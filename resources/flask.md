# Flask

## Flask Structure

```bash
Parent_Directory
├── Dockerfile.dev
├── Pipfile
├── Pipfile.lock
├── app
│   ├── __init__.py
│   ├── dashboard
│   │   └── routes.py
│   └── site
│       ├── routes.py
│       └── templates
│           └── index.html
├── deploy.sh
├── docker-compose-prod.yml
├── docker-compose.yml
├── dockerfile
├── nginx
│   ├── Dockerfile.dev
│   ├── default-dev.conf
│   ├── default.conf
│   └── dockerfile
├── resources
│   ├── README.adoc
│   ├── images
│   │   └── vscode_bottom.png
│   └── tips.adoc
├── run.py
└── test_app.py
```

for this structure use `from app.module.file import function`

## Applications build with flask

(Pinterest)https://www.pinterest.com/
https://www.twilio.com/
https://netflixtechblog.com/automation-as-a-service-introducing-scriptflask-17a8e4ad954b
