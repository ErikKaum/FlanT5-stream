import requests

url = "http://0.0.0.0:8000"
model_inputs = {
    'input_text': 'Answer the following yes/no question by reasoning step-by-step. Can you write a whole Haiku in a single tweet?'
    }

def get_stream(url):
    s = requests.Session()

    with s.post(url, json=model_inputs ,headers=None, stream=True) as resp:
        for line in resp.iter_lines():
            print(line)


def main():
    get_stream(url)

if __name__ == "__main__":
    main()
