## Docker

This application is containerized using Docker.

### Run with Docker

```bash
docker build -t devops-flask-app .
docker run -d -p 5000:5000 --name devops-app devops-flask-app


Save the file.

---

## Step 3 — Commit the change

Run:

```powershell
git status
--git push -u origin main
