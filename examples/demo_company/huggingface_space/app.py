"""
AI Workforce OS - Mini Content Agency
=====================================
HuggingFace Spaces Demo
"""

import gradio as gr
import os
from crewai import Agent, Task, Crew
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import List, Dict, Any, Optional

# Available models from AI Workforce OS collection
AVAILABLE_MODELS = {
    "Qwen2.5-3B (Fast)": "Qwen/Qwen2.5-3B-Instruct",
    "Qwen2.5-7B (Recommended)": "Qwen/Qwen2.5-7B-Instruct",
    "Qwen2.5-14B (High Quality)": "Qwen/Qwen2.5-14B-Instruct",
    "Qwen2.5-Coder-32B (Best)": "Qwen/Qwen2.5-Coder-32B-Instruct",
}

DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"


# ============ ROLES ============

class CompanyRoles:
    """AI Agent role definitions for the Mini Content Agency"""

    @staticmethod
    def research_analyst(llm: Optional[object] = None) -> Agent:
        return Agent(
            role='Research Analyst',
            goal='Gather comprehensive, accurate information on any topic',
            backstory='''You are an expert research analyst with years of experience
            in gathering and synthesizing information from various sources. You excel
            at finding relevant data, statistics, and insights that inform content creation.''',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def content_writer(llm: Optional[object] = None) -> Agent:
        return Agent(
            role='Content Writer',
            goal='Create engaging, well-structured content that resonates with the target audience',
            backstory='''You are a skilled content writer with expertise in creating
            compelling articles, blog posts, and marketing copy. You understand how to
            adapt your writing style to different audiences and purposes.''',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def seo_specialist(llm: Optional[object] = None) -> Agent:
        return Agent(
            role='SEO Specialist',
            goal='Optimize content for search engines while maintaining readability',
            backstory='''You are an SEO expert who understands search engine algorithms
            and user behavior. You know how to identify keywords, optimize content structure,
            and improve content visibility without sacrificing quality.''',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def social_media_manager(llm: Optional[object] = None) -> Agent:
        return Agent(
            role='Social Media Manager',
            goal='Create engaging social media content that drives engagement',
            backstory='''You are a social media expert who understands different platforms
            and their audiences. You create content that is platform-appropriate, engaging,
            and drives meaningful interactions.''',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )

    @staticmethod
    def qa_checker(llm: Optional[object] = None) -> Agent:
        return Agent(
            role='QA Checker',
            goal='Ensure all content meets quality standards before publication',
            backstory='''You are a meticulous quality assurance specialist who reviews
            content for accuracy, grammar, consistency, and adherence to brand guidelines.
            You have an eye for detail and ensure nothing subpar gets published.''',
            llm=llm,
            verbose=True,
            allow_delegation=False
        )


# ============ WORKFLOW ============

class ContentAgency:
    """Main workflow orchestrator for the Mini Content Agency"""

    def __init__(self, llm=None):
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
        if platforms is None:
            platforms = ['twitter', 'linkedin', 'facebook']

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


# ============ UI ============

agency = None

def get_llm(model_id: str = None, api_key: str = None):
    """Get configured LLM instance using HuggingFace Inference API"""
    hf_token = api_key or os.getenv('HUGGINGFACE_API_KEY') or os.getenv('HF_TOKEN')
    if not hf_token:
        raise ValueError("Please enter your HuggingFace API Key")

    model = model_id or DEFAULT_MODEL

    # Create endpoint with proper task specification
    llm = HuggingFaceEndpoint(
        repo_id=model,
        huggingfacehub_api_token=hf_token,
        task="text-generation",
        temperature=0.7,
        max_new_tokens=1024,
    )

    # Wrap in ChatHuggingFace for better compatibility with CrewAI
    return ChatHuggingFace(llm=llm)

def initialize_agency(model_name: str = None, api_key: str = None):
    """Initialize the content agency with selected model"""
    global agency
    try:
        if not api_key:
            return "Error: Please enter your HuggingFace API Key"

        model_id = AVAILABLE_MODELS.get(model_name, DEFAULT_MODEL)
        llm = get_llm(model_id=model_id, api_key=api_key)
        agency = ContentAgency(llm)
        return f"✅ Agency initialized with {model_name}!"
    except Exception as e:
        import traceback
        return f"Error: {str(e)}\n\nDetails: {traceback.format_exc()}"

def create_article_ui(topic, audience, word_count, progress=gr.Progress()):
    """UI wrapper for article creation"""
    if not agency:
        return "Please initialize the agency first!"

    try:
        progress(0, desc="Starting workflow...")
        progress(0.2, desc="Research in progress...")
        result = agency.create_article(
            topic=topic,
            target_audience=audience,
            word_count=int(word_count)
        )
        progress(1.0, desc="Complete!")

        output = f"""
## Article Created Successfully!

**Topic:** {result['topic']}
**Target Audience:** {result['audience']}
**Word Count:** {result['word_count']}

---

{result['article']}
"""
        return output

    except Exception as e:
        return f"Error: {str(e)}"

def create_social_ui(topic, platforms, progress=gr.Progress()):
    """UI wrapper for social campaign creation"""
    if not agency:
        return "Please initialize the agency first!"

    try:
        progress(0, desc="Starting campaign...")
        platform_list = [p.strip() for p in platforms.split(',')]
        progress(0.3, desc="Creating posts...")
        result = agency.create_social_campaign(
            topic=topic,
            platforms=platform_list
        )
        progress(1.0, desc="Complete!")

        output = f"""
## Social Campaign Created!

**Topic:** {result['topic']}
**Platforms:** {', '.join(result['platforms'])}

---

{result['posts']}
"""
        return output

    except Exception as e:
        return f"Error: {str(e)}"


# Build Gradio Interface
with gr.Blocks(title="AI Workforce OS - Demo Company") as demo:

    gr.Markdown("""
    # AI Workforce OS - Mini Content Agency

    **Your AI-Powered Content Team** | 100% Open Source Models

    **Team:** Research Analyst | Content Writer | SEO Specialist | Social Media Manager | QA Checker
    """)

    with gr.Accordion("Setup", open=True):
        gr.Markdown("""
        **Quick Start:**
        1. Enter your [HuggingFace API Key](https://huggingface.co/settings/tokens)
        2. Select a model
        3. Click 'Initialize Agency'
        """)

        with gr.Row():
            model_dropdown = gr.Dropdown(
                choices=list(AVAILABLE_MODELS.keys()),
                value="Qwen2.5-7B (Recommended)",
                label="Select Model"
            )
            api_key_input = gr.Textbox(
                label="HuggingFace API Key",
                placeholder="hf_xxxxxxxxxx",
                type="password"
            )

        init_btn = gr.Button("Initialize Agency", variant="primary")
        init_output = gr.Textbox(label="Status", interactive=False)
        init_btn.click(initialize_agency, inputs=[model_dropdown, api_key_input], outputs=init_output)

    gr.Markdown("---")

    with gr.Tabs():
        with gr.Tab("Create Article"):
            gr.Markdown("**Workflow:** Research -> Write -> SEO -> QA")

            with gr.Row():
                with gr.Column():
                    article_topic = gr.Textbox(
                        label="Article Topic",
                        placeholder="e.g., Benefits of AI in Healthcare",
                        lines=2
                    )
                    article_audience = gr.Textbox(
                        label="Target Audience",
                        value="general public"
                    )
                    article_words = gr.Number(
                        label="Word Count",
                        value=500,
                        minimum=100,
                        maximum=2000
                    )
                    article_btn = gr.Button("Create Article", variant="primary")

                with gr.Column():
                    article_output = gr.Markdown(label="Result")

            article_btn.click(
                create_article_ui,
                inputs=[article_topic, article_audience, article_words],
                outputs=article_output
            )

        with gr.Tab("Social Media Campaign"):
            gr.Markdown("**Workflow:** Research -> Create Posts -> QA")

            with gr.Row():
                with gr.Column():
                    social_topic = gr.Textbox(
                        label="Campaign Topic",
                        placeholder="e.g., Launch of new AI product",
                        lines=2
                    )
                    social_platforms = gr.Textbox(
                        label="Platforms (comma-separated)",
                        value="twitter, linkedin, facebook"
                    )
                    social_btn = gr.Button("Create Campaign", variant="primary")

                with gr.Column():
                    social_output = gr.Markdown(label="Result")

            social_btn.click(
                create_social_ui,
                inputs=[social_topic, social_platforms],
                outputs=social_output
            )

    gr.Markdown("""
    ---
    **AI Workforce OS** | [Website](https://aiworkforceos.org) | [Models](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models) | [GitHub](https://github.com/ekharitonov/aiworkforceos)
    """)

if __name__ == "__main__":
    demo.launch()
