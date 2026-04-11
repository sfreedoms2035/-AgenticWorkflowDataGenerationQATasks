import sys
import os
import json
import webbrowser
import html as web_html
import argparse

def generate_html(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)[0]
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Q&A Preview: {web_html.escape(data.get('training_data_id', 'Unknown'))}</title>
        <style>
            body {{ font-family: 'Inter', system-ui, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }}
            .container {{ max-width: 1000px; margin: 0 auto; }}
            .header {{ background-color: #1e293b; padding: 20px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border-left: 5px solid #3b82f6; }}
            .meta-tag {{ display: inline-block; background-color: #334155; padding: 4px 10px; border-radius: 4px; font-size: 0.85em; margin-right: 10px; margin-bottom: 10px; }}
            .turn {{ margin-bottom: 30px; border-radius: 8px; overflow: hidden; }}
            .turn.user {{ background-color: #1e293b; border-left: 4px solid #10b981; }}
            .turn.assistant {{ background-color: #1e293b; border-left: 4px solid #8b5cf6; }}
            .role {{ padding: 10px 15px; background-color: rgba(255, 255, 255, 0.05); font-weight: bold; text-transform: uppercase; font-size: 0.85em; letter-spacing: 1px; }}
            .role.user {{ color: #34d399; }}
            .role.assistant {{ color: #a78bfa; }}
            .content {{ padding: 15px; line-height: 1.6; white-space: pre-wrap; }}
            .reasoning {{ padding: 15px; background-color: rgba(0, 0, 0, 0.2); font-family: 'Fira Code', monospace; font-size: 0.85em; color: #94a3b8; border-top: 1px solid rgba(255,255,255,0.05); white-space: pre-wrap; }}
            .toggle-btn {{ background-color: #475569; color: white; border: none; padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 0.8em; margin-left: 10px; }}
        </style>
        <script>
            function toggleReasoning(index) {{
                const el = document.getElementById('reasoning-' + index);
                if (el.style.display === 'none') {{
                    el.style.display = 'block';
                }} else {{
                    el.style.display = 'none';
                }}
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>{web_html.escape(data.get('training_data_id', 'Unknown Task'))}</h2>
                <p><strong>Document:</strong> {web_html.escape(data.get('document', ''))}</p>
                <p><strong>Summary:</strong> {web_html.escape(data.get('summary', ''))}</p>
                <div style="margin-top: 15px;">
                    <span class="meta-tag">Role: {web_html.escape(data.get('affected_role', ''))}</span>
                    <span class="meta-tag">Difficulty: {web_html.escape(str(data.get('difficulty', '')))}</span>
                    <span class="meta-tag">Keywords: {web_html.escape(', '.join(data.get('key_words', [])))}</span>
                </div>
            </div>
            
            <h3>Conversation Flow</h3>
    """
    
    for i, turn in enumerate(data.get('conversations', [])):
        role = turn.get('role', 'unknown')
        content = turn.get('content', '')
        reasoning = turn.get('reasoning', '')
        
        reasoning_html = ""
        if reasoning and reasoning.strip() != "<think></think>":
            reasoning_html = f"""
                <div class="role" style="border-top: 1px solid rgba(255,255,255,0.05);">
                    INTERNAL MONOLOGUE <button class="toggle-btn" onclick="toggleReasoning({i})">Toggle</button>
                </div>
                <div class="reasoning" id="reasoning-{i}" style="display: none;">{web_html.escape(reasoning)}</div>
            """
            
        html += f"""
            <div class="turn {role}">
                <div class="role {role}">{role.upper()}</div>
                <div class="content">{web_html.escape(content)}</div>
                {reasoning_html}
            </div>
        """
        
    html += """
        </div>
    </body>
    </html>
    """
    return html

def main():
    parser = argparse.ArgumentParser(description="Render Q&A JSON to HTML preview")
    parser.add_argument("json_path", help="Path to generated JSON task")
    parser.add_argument("--open", action="store_true", help="Open in browser")
    args = parser.parse_args()
    
    if not os.path.exists(args.json_path):
        print(f"File not found: {args.json_path}")
        sys.exit(1)
        
    try:
        html = generate_html(args.json_path)
    except Exception as e:
        print(f"Failed to generate HTML: {e}")
        sys.exit(1)
        
    base_dir = os.path.dirname(args.json_path)
    html_name = os.path.basename(args.json_path).replace(".json", ".html")
    # Output to the project Eval/Previews directory
    # Assume script is in .agent/scripts and json is in Output/json
    project_root = os.path.dirname(os.path.dirname(base_dir))
    out_dir = os.path.join(project_root, "Eval", "Previews")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, html_name)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"Generated HTML preview: {out_path}")
    if args.open:
        webbrowser.open(f"file:///{out_path.replace(os.sep, '/')}")

if __name__ == "__main__":
    main()
