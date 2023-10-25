<hr/>
<h1 align="center">
CodersLand
</h1>

<p align="center">
  GitHub users' portfolios using Django and the GitHub API.
</p>

<p align="center">
    <!-- img alt="coderslands' License" src="https://img.shields.io/github/license/aratheunseen/codersland?style=for-the-badge">
    <img alt="coderslands' Workflow Status (with branch)" src="https://img.shields.io/github/actions/workflow/status/aratheunseen/codersland/django.yml?branch=main&label=Build&style=for-the-badge">
    <img alt="Top Language used in codersland" src="https://img.shields.io/github/languages/top/aratheunseen/codersland?style=for-the-badge&logo=dart&color=lightblue" -->
    <img alt="coderslands' Code Size" src="https://img.shields.io/github/languages/code-size/aratheunseen/codersland?style=for-the-badge">
</p>

<img src="https://github.com/aratheunseen/codersland/assets/62181222/2dde57a3-d801-4378-9915-8050448f0484" width="100%" alt="Portfolio of Linus Torvalds (@torvalds), founder of Linux Foundation">
<!-- img src="https://github.com/aratheunseen/codersland/assets/62181222/376f0cb2-4e66-4dd5-a2ce-1feb0a456582" width="100%" -->

<hr/>

<table align="center">
  <tr>
    <th>Home</th>
    <th>Feature</th>
  </tr>
  <tr>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/676dd8d0-0c35-4ea5-a12a-88624c4a509d"></td>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/029dab4c-3686-4203-a017-a6b398bf813a"></td>

  </tr>
  <tr>
    <th>Users' Bio</th>
    <th>Statistics</th>
  </tr>
  <tr>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/5e349078-c279-44b9-b7e5-daa1a3e5a634"></td>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/4d093f34-2133-43cf-8a5d-e1fb1b6defc3"></td>
  </tr>
  <tr>
    <th colspan="2">Organizations' Bio</th>
  </tr>
  <tr>
    <td colspan="2"><img src="https://github.com/aratheunseen/codersland/assets/62181222/05e2c812-e2a4-41f0-a749-0f0f486dff29"></td>
  </tr>
  <tr>
    <th>Connections</th>
    <th>CV Download</th>
  </tr>
  <tr>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/e9fcbf73-d07b-456c-914f-b6068974633b"></td>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/c41d76d0-0957-4dae-833d-49f62ee7af3e"></td>
  </tr>
  <tr>
    <th>Projects</th>
    <th>Projects' Details</th>
  </tr>
  <tr>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/480551d8-871c-4d61-ba3a-90448f1bebff"></td>
    <td><img src="https://github.com/aratheunseen/codersland/assets/62181222/2d4bd25f-6dfb-45b2-ac46-c30fd2780fb5"></td>
  </tr>
  <tr>
    <th colspan="2">Organizations' Projects' Details</th>
  </tr>
  <tr>
    <td colspan="2"><img src="https://github.com/aratheunseen/codersland/assets/62181222/33ae5eb5-50a7-4e03-98b0-92cb8d7b686c"></td>
  </tr>
</table>

<hr>

## Getting Started

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

Now you are all set to explore CodersLand, generate personalized portfolios, and see your or others' profiles, projects, connections and contributions in an automated and user-friendly manner.
