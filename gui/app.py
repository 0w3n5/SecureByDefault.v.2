import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

# === Auto-install python-terraform if missing ===
try:
    from python_terraform import Terraform
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-terraform"])
    from python_terraform import Terraform

TFVARS_PATH = "../terraform.tfvars"  # Adjust based on your project structure

def check_dependencies():
    # Check if terraform is installed
    if not shutil.which("terraform"):
        messagebox.showerror("Missing Dependency", "Terraform is not installed or not in PATH.")
        return False

    # Check if AWS CLI is installed
    if not shutil.which("aws"):
        messagebox.showerror("Missing Dependency", "AWS CLI is not installed or not in PATH.")
        return False

    return True

def deploy():
    if not check_dependencies():
        return

    region = region_var.get()
    email = email_var.get()
    project = project_var.get()
    profile = profile_var.get()
    environment = environment_var.get()

    # Generate terraform.tfvars
    with open(TFVARS_PATH, "w") as f:
        f.write(f'''aws_region = "{region}"
aws_profile = "{profile}"
alert_email_address = "{email}"
project = "{project}"
environment = "{environment}"
tags = {{
  Owner = "Terraform GUI"
  Project = "{project}"
  Environment = "{environment}"
}}
''')

    try:
        tf = Terraform(working_dir="..")
        tf.init()
        return_code, stdout, stderr = tf.apply(skip_plan=True, auto_approve=True)

        if return_code == 0:
            messagebox.showinfo("Success", "✅ Terraform deployed successfully!")
        else:
            messagebox.showerror("Error", f"❌ Terraform failed.\n\n{stderr}")

    except Exception as e:
        messagebox.showerror("Terraform Error", str(e))


# === GUI Setup ===
app = tk.Tk()
app.title("Secure Terraform Deployer")
app.geometry("400x350")

tk.Label(app, text="AWS Region").pack()
region_var = tk.StringVar(value="eu-west-2")
tk.Entry(app, textvariable=region_var).pack()

tk.Label(app, text="AWS CLI Profile").pack()
profile_var = tk.StringVar(value="default")
tk.Entry(app, textvariable=profile_var).pack()

tk.Label(app, text="Alert Email").pack()
email_var = tk.StringVar()
tk.Entry(app, textvariable=email_var).pack()

tk.Label(app, text="Project Name").pack()
project_var = tk.StringVar()
tk.Entry(app, textvariable=project_var).pack()

tk.Label(app, text="Environment").pack()
environment_var = tk.StringVar(value="dev")
tk.Entry(app, textvariable=environment_var).pack()

tk.Button(app, text="🚀 Deploy Infrastructure", command=deploy).pack(pady=15)

app.mainloop()
