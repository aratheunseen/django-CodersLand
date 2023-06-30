<hr/>
<h1 align="center">
CodersLand
</h1>

<p align="center">
  Auto-generate GitHub users' portfolios using Django and the GitHub API.
</p>

<p align="center">
    <!-- img alt="coderslands' License" src="https://img.shields.io/github/license/aratheunseen/codersland?style=for-the-badge">
    <img alt="coderslands' Workflow Status (with branch)" src="https://img.shields.io/github/actions/workflow/status/aratheunseen/codersland/django.yml?branch=main&label=Build&style=for-the-badge" -->
    <img alt="Top Language used in codersland" src="https://img.shields.io/github/languages/top/aratheunseen/codersland?style=for-the-badge&logo=dart&color=lightblue">
    <img alt="coderslands' Code Size" src="https://img.shields.io/github/languages/code-size/aratheunseen/codersland?style=for-the-badge">
</p>

<img src="https://github.com/aratheunseen/codersland/assets/62181222/2dde57a3-d801-4378-9915-8050448f0484" width="100%">
<!-- img src="https://github.com/aratheunseen/codersland/assets/62181222/376f0cb2-4e66-4dd5-a2ce-1feb0a456582" width="100%" -->

<hr/>

## Getting Started

Getting Started with CodersLand

To get started with CodersLand, follow these steps:

1. Clone the Repository: Clone the CodersLand repository from GitHub using the command:
   ```
   git clone https://github.com/aratheunseen/codersland.git
   ```

2. Set up a Virtual Environment: Create a virtual environment for the project to keep the dependencies isolated. You can use `venv` for this purpose.

3. Install Dependencies: Navigate to the project directory and install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

4. Configure GitHub API Access: Obtain a GitHub API access token by creating a new personal access token in your GitHub account settings. Rename the `config-demo.py` file to `config.py` in the `main` folder  and update `SITE_NAME`, `SITE_URL` and the `GITHUB_PAT` variable with your private access token.

5. Run Database Migrations: Apply the database migrations using the following command:
   ```
   python manage.py migrate
   ```

6. Start the Development Server: Launch the development server with the command:
   ```
   python manage.py runserver
   ```

7. Access CodersLand: Open your web browser and visit `http://localhost:8000` to access the CodersLand application.

8. Generate Your Portfolio: Enter your GitHub username in the provided field and click the "Generate Portfolio" button. CodersLand will fetch your GitHub data using the GitHub API and display your portfolio.

Now you are all set to explore CodersLand, generate personalized portfolios, and showcase your coding projects and contributions in an automated and user-friendly manner. Happy coding!
