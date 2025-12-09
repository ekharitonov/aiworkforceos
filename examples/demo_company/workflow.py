"""
AI Workforce OS - Demo Company Workflow
========================================

This module defines how tasks flow through the AI company.
"""

from crewai import Task, Crew
from typing import List, Dict, Any
from roles import CompanyRoles

class ContentAgency:
    """Main workflow orchestrator for the Mini Content Agency"""
    
    def __init__(self, llm=None):
        """Initialize the agency with all roles"""
        self.llm = llm
        self.roles = CompanyRoles()
        
        # Initialize all agents
        self.researcher = self.roles.research_analyst(llm)
        self.writer = self.roles.content_writer(llm)
        self.seo = self.roles.seo_specialist(llm)
        self.social = self.roles.social_media_manager(llm)
        self.qa = self.roles.qa_checker(llm)
    
    def create_article(self, topic: str, target_audience: str = "general public", 
                      word_count: int = 500) -> Dict[str, Any]:
        """
        Create a complete article workflow
        
        Args:
            topic: The article topic
            target_audience: Who the article is for
            word_count: Target word count
            
        Returns:
            Dictionary with article content and metadata
        """
        
        # Task 1: Research
        research_task = Task(
            description=f"""Research the topic: {topic}
            
            Requirements:
            - Find 5-7 key points about the topic
            - Include relevant statistics or data
            - Identify current trends or developments
            - Note credible sources
            
            Target audience: {target_audience}""",
            expected_output="A comprehensive research summary with key findings and sources",
            agent=self.researcher
        )
        
        # Task 2: Write article
        writing_task = Task(
            description=f"""Write a {word_count}-word article about: {topic}
            
            Requirements:
            - Use the research findings
            - Target audience: {target_audience}
            - Include: introduction, main points, conclusion
            - Make it engaging and easy to read
            - Use active voice and clear language""",
            expected_output=f"A well-structured {word_count}-word article",
            agent=self.writer,
            context=[research_task]
        )
        
        # Task 3: SEO optimization
        seo_task = Task(
            description=f"""Optimize the article for SEO
            
            Requirements:
            - Suggest 5-7 relevant keywords
            - Recommend title variations
            - Suggest meta description
            - Identify internal linking opportunities
            - Ensure content is search-friendly""",
            expected_output="SEO recommendations and optimized version",
            agent=self.seo,
            context=[writing_task]
        )
        
        # Task 4: Quality check
        qa_task = Task(
            description="""Review the article for quality
            
            Check for:
            - Grammatical errors
            - Factual accuracy
            - Logical flow
            - Readability
            - Consistency
            
            Provide specific feedback if issues are found.""",
            expected_output="Quality assessment report and final version",
            agent=self.qa,
            context=[writing_task, seo_task]
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[self.researcher, self.writer, self.seo, self.qa],
            tasks=[research_task, writing_task, seo_task, qa_task],
            verbose=2
        )
        
        result = crew.kickoff()
        
        return {
            'article': result,
            'topic': topic,
            'audience': target_audience,
            'word_count': word_count
        }
    
    def create_social_campaign(self, topic: str, platforms: List[str] = None) -> Dict[str, Any]:
        """
        Create social media campaign
        
        Args:
            topic: Campaign topic
            platforms: List of platforms (e.g., ['twitter', 'linkedin', 'facebook'])
            
        Returns:
            Dictionary with posts for each platform
        """
        if platforms is None:
            platforms = ['twitter', 'linkedin', 'facebook']
        
        # Task 1: Research
        research_task = Task(
            description=f"""Research the topic: {topic}
            
            Focus on:
            - Current conversations and trends
            - Engaging angles
            - Key talking points
            - Relevant hashtags""",
            expected_output="Social media research summary",
            agent=self.researcher
        )
        
        # Task 2: Create posts
        social_task = Task(
            description=f"""Create social media posts about: {topic}
            
            Create posts for: {', '.join(platforms)}
            
            Requirements:
            - Platform-specific format and length
            - Engaging hooks
            - Clear call-to-action
            - Relevant hashtags
            - Emojis where appropriate""",
            expected_output=f"Social media posts for {len(platforms)} platforms",
            agent=self.social,
            context=[research_task]
        )
        
        # Task 3: Quality check
        qa_task = Task(
            description="""Review social posts
            
            Check for:
            - Grammar and spelling
            - Brand voice consistency
            - Platform appropriateness
            - Engagement potential""",
            expected_output="Reviewed and approved social posts",
            agent=self.qa,
            context=[social_task]
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[self.researcher, self.social, self.qa],
            tasks=[research_task, social_task, qa_task],
            verbose=2
        )
        
        result = crew.kickoff()
        
        return {
            'posts': result,
            'topic': topic,
            'platforms': platforms
        }
    
    def optimize_content(self, existing_content: str) -> Dict[str, Any]:
        """
        Optimize existing content for better performance
        
        Args:
            existing_content: The content to optimize
            
        Returns:
            Dictionary with optimized content and suggestions
        """
        
        # Task 1: SEO analysis
        seo_task = Task(
            description=f"""Analyze and optimize this content:
            
            {existing_content}
            
            Provide:
            - SEO score (1-10)
            - Keyword suggestions
            - Content structure improvements
            - Meta data recommendations""",
            expected_output="SEO analysis and optimization plan",
            agent=self.seo
        )
        
        # Task 2: Rewrite
        writing_task = Task(
            description="""Rewrite the content based on SEO recommendations
            
            Keep:
            - Core message
            - Key facts
            
            Improve:
            - Structure
            - Readability
            - SEO optimization""",
            expected_output="Optimized content version",
            agent=self.writer,
            context=[seo_task]
        )
        
        # Task 3: Quality check
        qa_task = Task(
            description="""Compare original and optimized versions
            
            Ensure:
            - Message integrity
            - Factual accuracy
            - Quality improvements
            - No errors introduced""",
            expected_output="Final optimized content with comparison",
            agent=self.qa,
            context=[writing_task]
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[self.seo, self.writer, self.qa],
            tasks=[seo_task, writing_task, qa_task],
            verbose=2
        )
        
        result = crew.kickoff()
        
        return {
            'optimized_content': result,
            'original_content': existing_content
        }


# Workflow metadata for UI
WORKFLOW_TEMPLATES = {
    'create_article': {
        'name': 'Create Article',
        'description': 'Research, write, optimize, and QA check an article',
        'agents': ['Research Analyst', 'Content Writer', 'SEO Specialist', 'QA Checker'],
        'estimated_time': '5-10 minutes',
        'inputs': {
            'topic': 'text',
            'target_audience': 'text',
            'word_count': 'number'
        }
    },
    'create_social_campaign': {
        'name': 'Social Media Campaign',
        'description': 'Create posts for multiple social platforms',
        'agents': ['Research Analyst', 'Social Media Manager', 'QA Checker'],
        'estimated_time': '3-5 minutes',
        'inputs': {
            'topic': 'text',
            'platforms': 'multiselect'
        }
    },
    'optimize_content': {
        'name': 'Optimize Content',
        'description': 'Improve existing content for better SEO and readability',
        'agents': ['SEO Specialist', 'Content Writer', 'QA Checker'],
        'estimated_time': '3-5 minutes',
        'inputs': {
            'existing_content': 'textarea'
        }
    }
}