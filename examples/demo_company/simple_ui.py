"""
AI Workforce OS - Demo Company UI
==================================

Simple user interface for interacting with the AI company.
Built with Gradio for ease of use.
"""

import gradio as gr
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint
from workflow import ContentAgency, WORKFLOW_TEMPLATES

# Load environment variables
load_dotenv()

# Available models from AI Workforce OS collection
AVAILABLE_MODELS = {
    "Qwen2.5-3B (Fast, 8GB RAM)": "Qwen/Qwen2.5-3B-Instruct",
    "Qwen2.5-7B (Recommended)": "Qwen/Qwen2.5-7B-Instruct",
    "Qwen2.5-14B (High Quality)": "Qwen/Qwen2.5-14B-Instruct",
    "Qwen2.5-Coder-32B (Best Quality)": "Qwen/Qwen2.5-Coder-32B-Instruct",
}

DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"

# Initialize LLM
def get_llm(model_id: str = None, api_key: str = None):
    """Get configured LLM instance using HuggingFace Inference API"""
    # Try to get API key from parameter, then environment
    hf_token = api_key or os.getenv('HUGGINGFACE_API_KEY')
    if not hf_token:
        raise ValueError("Please set HUGGINGFACE_API_KEY in Codespaces Secrets or .env file")

    model = model_id or DEFAULT_MODEL

    return HuggingFaceEndpoint(
        repo_id=model,
        huggingfacehub_api_token=hf_token,
        temperature=0.7,
        max_new_tokens=1024,
    )

# Initialize agency
agency = None

def initialize_agency(model_name: str = None, api_key: str = None):
    """Initialize the content agency with selected model"""
    global agency
    try:
        # Get model ID from name
        model_id = AVAILABLE_MODELS.get(model_name, DEFAULT_MODEL)
        llm = get_llm(model_id=model_id, api_key=api_key if api_key else None)
        agency = ContentAgency(llm)
        return f"✅ Agency initialized with {model_id}!"
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
    
    with gr.Blocks(title="AI Workforce OS - Demo Company") as demo:
        
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
            1. Set `HUGGINGFACE_API_KEY` in [Codespaces Secrets](https://github.com/settings/codespaces) or enter below
            2. Select a model from the dropdown
            3. Click 'Initialize Agency'

            **Models from [AI Workforce OS Collection](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models)** - 100% Open Source!
            """)

            with gr.Row():
                model_dropdown = gr.Dropdown(
                    choices=list(AVAILABLE_MODELS.keys()),
                    value="Qwen2.5-7B (Recommended)",
                    label="Select Model"
                )
                api_key_input = gr.Textbox(
                    label="HuggingFace API Key (optional if set in Codespaces Secrets)",
                    placeholder="hf_xxxxxxxxxx",
                    type="password"
                )

            init_btn = gr.Button("🚀 Initialize Agency", variant="primary")
            init_output = gr.Textbox(label="Status", interactive=False)
            init_btn.click(initialize_agency, inputs=[model_dropdown, api_key_input], outputs=init_output)
        
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
        - **100% Open Source** models from HuggingFace

        **Cost:** FREE with HuggingFace Inference API (rate limits apply)

        **Learn more:** [AI Workforce OS](https://aiworkforceos.org) | [Model Collection](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models)
        """)
    
    return demo


if __name__ == "__main__":
    demo = build_interface()
    demo.launch(share=True, server_name="0.0.0.0", server_port=8080)
