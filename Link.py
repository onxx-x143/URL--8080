import os
import time
import sys
import subprocess
import shutil

# Colors define kar rahe hain
R = '\033[91m'  # Red
G = '\033[98m'  # Green
Y = '\033[93m'  # Yellow
C = '\033[96m'  # Cyan
M = '\033[95m'  # Magenta
W = '\033[96m'   # Reset (White)

def clear_screen():
    # Windows ke liye 'cls' aur Linux/Mac/Termux ke liye 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    # Badi Cat 😺 aur Colorful Text Banner
    banner = f"""
{R}              ⣀⣤⣶⣿⣿⣷⣆              
            ⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⣤⣶⣾⣿⣿⣶       =================
          ⢦⣿⣻⣿⣿⣿⣿⡿⣫⣷⣿⣿⣿⣿⣿⣿⠟⠁            URL Link 🖇️ 
          ⠘⣿⣿⣿⣿⡿⣣⡿⣻⣿⣿⣿⣿⣿⡟               localhost:8080
           ⠸⣿⣿⣿⣾⣫⣾⣿⣿⣿⣿⣿⣿⣧⣐⠄          =================
            ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡬⢧⠤       
          ⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣴⣾⣿⣿⣿⡶            by onxx-x143
   ⢠⠄     ⣾⣿⡿⠟⢉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⣿⣇   
  ⢀⡟⢧     ⠉⠁   ⠉⠙⣿⣿⣿⣿⠻⢟⣿⣾⣿⣿⣿⣿⣿⣯⡉            IG _insrnx_
  ⣾⡳⠘⣇            ⠙⠛⠁⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦          
 ⣰⡏⢁⠴⠹⡄             ⣰⣾⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣆ 
⢠⡿⠃⡏⢠⡏⢳⡀            ⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡄
⢿⡑⣞⡈⡚⢠⠖⣧⡀  ⢀⣠⣤⣾⣿⣶⣶⣶⣄ ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠇⠱
⠈⢷⣀⠨⢐⠎⠴⢈⢧ ⠈⠙⠋⢸⡿⢁⣉⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣟⠜  
 ⠈⢿⡀⢮⢐⠃⡖⣸⠧⢀⣀⣀⢋⡁⠚⠋⢥⡀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⣿       
  ⠈⣷⡀⠞⡵⢢⣿⡿⣾⣿⣿⡿⣿⣿⣿⣿⣿⣤⣘⠻⢿⣿⣿⣿⣿⣿⣇⢿ ⠁   
   ⠈⣷ ⠁⣿⣿⣷⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣾⣿⣿⣿⣿⣿⠈     
    ⠘⣧⡹⣾⡿⣼⣿⣾⣿⡯⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡇⢿      
     ⠘⣿⠿⡣⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠃⠘⡼⡇⠿⢋⢿⠑⠡⠸      
      ⠈⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁ ⠁⢡  ⠘
{W}"""
    print(banner)

def start_tunnel():
    clear_screen()
    show_banner()
    
    # Check karna ki system mein SSH command available hai ya nahi
    if not shutil.which("ssh"):
        print(f"{R}❌ Error: Aapke system mein 'ssh' tool nahi mila!{W}")
        print(f"{Y}💡 Termux me install karne ke liye type karein: pkg install openssh{W}")
        sys.exit(1)

    # Colorful Input
    port = input(f"{C}👉local URL (Jaise: 8080): {W}")
    
    # Validate karna ki port number valid hai
    if not port.isdigit() or not (1 <= int(port) <= 65535):
        print(f"\n{R}❌ Bhai, sirf ek valid port number type karo (1 se 65535 ke beech, eg. 8080){W}")
        sys.exit(1)
        
    print(f"\n{Y}⏳ Port {port} ko internet par live kiya ja raha hai...{W}")
    print(f"{G}🔗 Niche terminal mein ek link aayegi (jaise: https://xxxxx.lhr.life) jo SIDHA open hogi.{W}")
    print(f"{R}🛑 Band karne ke liye 'Ctrl + C' dabana.{W}\n")
    time.sleep(2)
    
    # Direct open without Ads server
    command =[
        "ssh", 
        "-o", "StrictHostKeyChecking=no", 
        "-R", f"80:localhost:{port}", 
        "nokey@localhost.run"
    ]
    
    try:
        # Tunnel start karna
        subprocess.run(command)
    except KeyboardInterrupt:
        print(f"\n\n{R}❌ Tool Stop Kar Diya Gaya Hai.{W}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}❌ Ek error aayi: {e}{W}")
        sys.exit(1)

if __name__ == '__main__':
    start_tunnel()
