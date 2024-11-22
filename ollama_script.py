import subprocess

file_path = 'files/downloaded-file.txt'


def ask_with_rag(question):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    command = ['ollama', 'run', 'llama3.2', question, file_content]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return f"Error: {result.stderr.strip()}"

def main():
    question = input("What do you want to know? : ")

    response_with_rag = ask_with_rag(question)
    print(response_with_rag)
if __name__ == "__main__":
    main()