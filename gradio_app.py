import gradio as gr
import openai
import requests
from bs4 import BeautifulSoup

# Set up OpenAI API key
openai.api_key = "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"

# Function to generate domain name suggestions using ChatGPT
def generate_domain_suggestions(keyword, description, number=10):
    # Call OpenAI API to generate domain name suggestions
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate {number} domain name suggestions containing the keyword '{keyword}'. This domain will be used for a product that: {description}. Show each domain in one line. Domain sugestions must be creative and different from others. Never suggest domains that diffent only in extension part.",
        max_tokens=1024,
        stop=None,
        temperature=0.5
    )
    domain_suggestions = response.choices[0].text.strip().split("\n")
    return domain_suggestions

# Function to check if a domain is available for purchase
def check_domain_availability(domain):
    response = requests.get(f"https://www.whois.com/whois/{domain}")
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find("div", {"id": "registryData"})
    if result is not None:
        return False
    else:
        return True

# Backend Django
def get_domain_suggestions(keyword, description):
    # Bước 1: generate keyword sử dụng ChatGPT
    print("Domain suggestions:")
    domain_suggestions = generate_domain_suggestions(keyword, description)

    # Bước 2: in ra danh sách domain được ChatGPT gợi ý
    for domain in domain_suggestions:
        print(domain)

    # Bước 3: kiểm tra domain có sẵn hay không
    print()
    print("Checking domain availability...")

    available_domains = []
    unavailable_domains = []
    output = ""
    for domain in domain_suggestions:
        if check_domain_availability(domain):
            available_domains.append(domain)
            output += domain + "\n"
            print(f"{domain}: Available")
        else:
            unavailable_domains.append(domain)
            print(f"{domain}: Unavailable")

    return output


# Giao diện Gradio
def main(keyword, description):
    # Gọi phần mềm xử lý ở backend (Django)
    response = get_domain_suggestions(keyword, description)
    return response

if __name__ == "__main__":
    # create a gradio UI to run main function and display the result. Have loading animation while waiting for result. All guiding text is in vietnamese
    # input variable should have vietnamese label description to guide user to use the app
    # output variable should have vietnamese label and description to guide user to use the app
    # display progress bar while waiting for result

    iface = gr.Interface(fn=main, inputs=[gr.inputs.Textbox(label="Keyword"),
                                          gr.inputs.Textbox(label="Mô tả sản phẩm")], outputs=[gr.outputs.Textbox(label="Danh sách Domain có thể mua")], capture_session=True, title="Domain Hunter App", description="Ứng dụng tìm tên miền cho sản phẩm của bạn. Hãy nhập từ khóa và mô tả sản phẩm của bạn, ứng dụng sẽ gợi ý cho bạn các tên miền phù hợp")




    iface.launch(share=True)



