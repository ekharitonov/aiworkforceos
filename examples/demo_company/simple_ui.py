"""
AI Workforce OS - Demo Company UI
==================================

Simple user interface for interacting with the AI company.
Built with Gradio for ease of use.
"""

import gradio as gr
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from workflow import ContentAgency, WORKFLOW_TEMPLATES

# Load environment variables
load_dotenv()

# Initialize LLM
def get_llm():
    """Get configured LLM instance"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("Please set OPENAI_API_KEY in .env file")
    
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7,
        api_key=api_key
    )

# Initialize agency
agency = None

def initialize_agency():
    """Initialize the content agency"""
    global agency
    try:
        llm = get_llm()
        agency = ContentAgency(llm)
        return "✅ Agency initialized successfully!"
    except Exception as e:
        return f"❌ Error: {str(e)}"

def create_article_ui(topic, audience, word_count, progress=gr.Progress()):
    """UI wrapper for article creation"""
    if not agency:
        return "❌ Please initialize the agency first!"
    
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
## ✅ Article Created Successfully!

**Topic:** {result['topic']}
**Target Audience:** {result['audience']}
**Word Count:** {result['word_count']}

---

{result['article']}
"""
        return output
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

def create_social_ui(topic, platforms, progress=gr.Progress()):
    """UI wrapper for social campaign creation"""
    if not agency:
        return "❌ Please initialize the agency first!"
    
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
## ✅ Social Campaign Created!

**Topic:** {result['topic']}
**Platforms:** {', '.join(result['platforms'])}

---

{result['posts']}
"""
        return output
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

def optimize_content_ui(content, progress=gr.Progress()):
    """UI wrapper for content optimization"""
    if not agency:
        return "❌ Please initialize the agency first!"
    
    try:
        progress(0, desc="Analyzing content...")
        
        progress(0.3, desc="Optimizing...")
        result = agency.optimize_content(existing_content=content)
        
        progress(1.0, desc="Complete!")
        
        output = f"""
## ✅ Content Optimized!

### Original Content:
{result['original_content'][:200]}...

---

### Optimized Version:
{result['optimized_content']}
"""
        return output
        
    except Exception as e:
        return f"❌ Error: {str(e)}"


# Build Gradio Interface
def build_interface():
    """Build the complete Gradio interface"""
    
    with gr.Blocks(title="AI Workforce OS - Demo Company", theme=gr.themes.Soft()) as demo:
        
        gr.Markdown("""
        # 🤖 AI Workforce OS - Mini Content Agency
        
        **Your AI-Powered Content Team**
        
        👥 **Team Structure:**
        - 🔬 Research Analyst
        - ✍️ Content Writer
        - 🎯 SEO Specialist
        - 📱 Social Media Manager
        - ✅ QA Checker
        """)
        
        # Setup section
        with gr.Accordion("⚙️ Setup", open=True):
            gr.Markdown("""
            **Before starting:**
            1. Create a `.env` file in this directory
            2. Add your OpenAI API key: `OPENAI_API_KEY=your_key_here`
            3. Click 'Initialize Agency' below
            """)
            
            init_btn = gr.Button("🚀 Initialize Agency", variant="primary")
            init_output = gr.Textbox(label="Status", interactive=False)
            init_btn.click(initialize_agency, outputs=init_output)
        
        gr.Markdown("---")
        
        # Workflows
        with gr.Tabs():
            
            # Article Creation Tab
            with gr.Tab("📝 Create Article"):
                gr.Markdown("""
                **Workflow:** Research → Write → SEO → QA
                
                The team will research your topic, write an article, optimize it for SEO, and check quality.
                """)
                
                with gr.Row():
                    with gr.Column():
                        article_topic = gr.Textbox(
                            label="Article Topic",
                            placeholder="e.g., Benefits of AI in Healthcare",
                            lines=2
                        )
                        article_audience = gr.Textbox(
                            label="Target Audience",
                            value="general public",
                            placeholder="e.g., healthcare professionals, general public"
                        )
                        article_words = gr.Number(
                            label="Word Count",
                            value=500,
                            minimum=100,
                            maximum=2000
                        )
                        article_btn = gr.Button("🚀 Create Article", variant="primary")
                    
                    with gr.Column():
                        article_output = gr.Markdown(label="Result")
                
                article_btn.click(
                    create_article_ui,
                    inputs=[article_topic, article_audience, article_words],
                    outputs=article_output
                )
            
            # Social Campaign Tab
            with gr.Tab("📱 Social Media Campaign"):
                gr.Markdown("""
                **Workflow:** Research → Create Posts → QA
                
                The team will research your topic and create platform-specific social media posts.
                """)
                
                with gr.Row():
                    with gr.Column():
                        social_topic = gr.Textbox(
                            label="Campaign Topic",
                            placeholder="e.g., Launch of new AI product",
                            lines=2
                        )
                        social_platforms = gr.Textbox(
                            label="Platforms (comma-separated)",
                            value="twitter, linkedin, facebook",
                            placeholder="twitter, linkedin, facebook, instagram"
                        )
                        social_btn = gr.Button("🚀 Create Campaign", variant="primary")
                    
                    with gr.Column():
                        social_output = gr.Markdown(label="Result")
                
                social_btn.click(
                    create_social_ui,
                    inputs=[social_topic, social_platforms],
                    outputs=social_output
                )
            
            # Content Optimization Tab
            with gr.Tab("🎯 Optimize Content"):
                gr.Markdown("""
                **Workflow:** SEO Analysis → Rewrite → QA
                
                The team will analyze and optimize your existing content for better performance.
                """)
                
                with gr.Row():
                    with gr.Column():
                        optimize_input = gr.Textbox(
                            label="Existing Content",
                            placeholder="Paste your content here...",
                            lines=10
                        )
                        optimize_btn = gr.Button("🚀 Optimize Content", variant="primary")
                    
                    with gr.Column():
                        optimize_output = gr.Markdown(label="Result")
                
                optimize_btn.click(
                    optimize_content_ui,
                    inputs=[optimize_input],
                    outputs=optimize_output
                )
        
        gr.Markdown("""
        ---
        
        ### 📊 About This Demo
        
        This is a working prototype of an AI-powered content agency with:
        - **5 AI Agents** with specialized roles
        - **3 Workflows** for different content needs
        - **Autonomous collaboration** between agents
        
        **Cost per task:** ~$0.05-0.15 (using GPT-3.5-turbo)
        
        **Learn more:** [AI Workforce OS](https://aiworkforceos.org)
        """)
    
    return demo


if __name__ == "__main__":
    demo = build_interface()
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
