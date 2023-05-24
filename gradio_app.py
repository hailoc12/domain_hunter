import gradio as gr
from django.core.wsgi import get_wsgi_application

# Giao diện Gradio
def greet(keyword, description):
    # Gọi phần mềm xử lý ở backend (Django)
    response = get_domain_suggestions(keyword, description)
    return response

iface = gr.Interface(fn=greet, inputs=["text", "text"], outputs="text")
iface.launch()

# Backend Django
def get_domain_suggestions(keyword, description):
    # Xử lý logic ở backend để tạo và kiểm tra domain
    # Trả về danh sách domain gợi ý
    return "Domain suggestions"

application = get_wsgi_application()
