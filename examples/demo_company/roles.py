"""
AI Workforce OS - Demo Company Roles
====================================

This module defines the roles for our Mini Content Agency.
Each role has specific responsibilities and expertise.
"""

from crewai import Agent
from typing import Optional

class CompanyRoles:
    """Defines all AI agent roles in the company"""
    
    @staticmethod
    def research_analyst(llm: Optional[object] = None) -> Agent:
        """
        Research Analyst - Information gathering expert
        
        Responsibilities:
        - Find relevant information and data
        - Verify facts and sources
        - Provide comprehensive research summaries
        """
        return Agent(
            role='Research Analyst',
            goal='Gather accurate and comprehensive information on any given topic',
            backstory="""You are an expert research analyst with 10+ years of experience.
            You excel at finding reliable sources, verifying facts, and synthesizing 
            complex information into clear insights. You always cite your sources and 
            distinguish between facts and opinions.""",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
    
    @staticmethod
    def content_writer(llm: Optional[object] = None) -> Agent:
        """
        Content Writer - Professional writing expert
        
        Responsibilities:
        - Write engaging articles and content
        - Maintain consistent tone and style
        - Follow content guidelines
        """
        return Agent(
            role='Content Writer',
            goal='Create engaging, well-structured content that resonates with the target audience',
            backstory="""You are a professional content writer with expertise in 
            creating compelling narratives. You understand how to engage readers,
            structure arguments effectively, and adapt your writing style to 
            different audiences and formats.""",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
    
    @staticmethod
    def seo_specialist(llm: Optional[object] = None) -> Agent:
        """
        SEO Specialist - Search optimization expert
        
        Responsibilities:
        - Optimize content for search engines
        - Suggest relevant keywords
        - Improve content discoverability
        """
        return Agent(
            role='SEO Specialist',
            goal='Optimize content for maximum search engine visibility and organic reach',
            backstory="""You are an SEO expert who understands search algorithms,
            keyword research, and content optimization. You know how to balance 
            SEO requirements with readability and user experience.""",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
    
    @staticmethod
    def social_media_manager(llm: Optional[object] = None) -> Agent:
        """
        Social Media Manager - Social content expert
        
        Responsibilities:
        - Create engaging social media posts
        - Adapt content for different platforms
        - Maximize engagement and reach
        """
        return Agent(
            role='Social Media Manager',
            goal='Create compelling social media content that drives engagement',
            backstory="""You are a social media expert who understands platform-specific
            best practices, audience psychology, and viral content patterns. You know
            how to craft posts that generate engagement and conversions.""",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )
    
    @staticmethod
    def qa_checker(llm: Optional[object] = None) -> Agent:
        """
        QA Checker - Quality assurance expert
        
        Responsibilities:
        - Check for errors and inconsistencies
        - Verify facts and claims
        - Ensure quality standards
        """
        return Agent(
            role='QA Checker',
            goal='Ensure all content meets quality standards and is error-free',
            backstory="""You are a meticulous QA specialist with an eye for detail.
            You catch grammatical errors, factual inconsistencies, and logical flaws.
            You ensure every piece of content meets professional standards before 
            it goes live.""",
            llm=llm,
            verbose=True,
            allow_delegation=False
        )


# Role hierarchy and interaction patterns
ROLE_HIERARCHY = {
    'research_analyst': {
        'level': 1,
        'reports_to': 'human_ceo',
        'delegates_to': []
    },
    'content_writer': {
        'level': 2,
        'reports_to': 'human_editor',
        'delegates_to': ['research_analyst']
    },
    'seo_specialist': {
        'level': 2,
        'reports_to': 'human_editor',
        'delegates_to': ['content_writer']
    },
    'social_media_manager': {
        'level': 2,
        'reports_to': 'human_editor',
        'delegates_to': ['content_writer']
    },
    'qa_checker': {
        'level': 3,
        'reports_to': 'human_editor',
        'delegates_to': []
    }
}

# Standard workflows
WORKFLOWS = {
    'article_creation': [
        'research_analyst',
        'content_writer',
        'seo_specialist',
        'qa_checker'
    ],
    'social_media_campaign': [
        'research_analyst',
        'social_media_manager',
        'qa_checker'
    ],
    'content_optimization': [
        'seo_specialist',
        'content_writer',
        'qa_checker'
    ]
}