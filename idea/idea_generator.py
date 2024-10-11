from idea_formatter import xml_to_json

from openai import OpenAI


def read_prompt():
    with open("doc/content_idea_gen_prompt", "r") as prompt_file:
        prompt = prompt_file.read()

    return prompt


def openai_request(request_content):
    try:
        client = OpenAI(api_key="sk-gW5gwWrucHPXcyMcrm9wj795BtM1uERiOtK-P44nZ4T3BlbkFJkNdoWKm0bZXW06UCWlBU60w_77RToC7hI-Hm11600A")

        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": request_content}
        ]
        )

        return completion.choices[0].message

    except Exception as e:
        print(e)



if __name__ == "__main__":
    pr = read_prompt()
    print(openai_request(pr))