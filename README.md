# Invest blog (qraphql)

App represents a pet-project for studying basics of graphql.

It has 4 models: Category, Course, Mentor, Student. Every course balongs to a certain category. Every mentor and student could be assigned to several courses.

Access to graphql panel is provided via /graphql url of your main domain (localhost for local development). It allows to you to perform Graphql queries to reveive data in json format.  

For example, the code below finds all categories, related courses, mentors and students assigned to every single course.

```console
query {
  allCategories {
    title,
    courses {
      title, 
      mentors {user {username}, status},
      students {user {username}, status}
    },
  },
}
```

## Install

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/invest-blog-graphql
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

4. Install requirements by command:
```console
pip install -r requirements.txt
```

5. Rename `.env.example` to `.env` and define your proper values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project django secret key
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)

## Launch

1. Make migrations
```console
python3 manage.py migrate
```

2. Run server
```console
python3 manage.py runserver
```

Graphql interface would be accessible via localhost/graphql (if you install it locally) url.