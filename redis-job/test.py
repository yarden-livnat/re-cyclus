import redis
import rom
from rom import util
import six
from .model import Job, Task
from datetime import datetime

cache =  redis.Redis(host='localhost', db=0)
rom.util.set_connection_settings(host='localhost', db=7)

# util.CONNECTION = redis.Redis(db=9)
# connect = util._connect

# redis = connect(None)


# def global_setup():
#     c = connect(None)
#     for p in ('RestrictA*', 'RestrictB*'):
#         keys = c.keys(p)
#         if keys:
#             c.delete(*keys)
#     from rom.columns import MODELS
#     Model = MODELS['Model']
#     for k, v in MODELS.copy().items():
#         if v is not Model:
#             del MODELS[k]


def run():
    # global_setup()
    create('yarden', 'foo')
    create('yarden', 'bar')
    create('yarden', 'foo')
    check()


def create_jobid(username, project_name):
    counter = f'counter:{username}:{project_name}'
    n = cache.incr(counter)
    return f'{username}:{project_name}-{n}'


# def get_user(username):
#     u = User.get_by(name=username)
#     if u is None:
#         print('create user:', username)
#         u = User(name=username)
#     return u
#
#
# def get_project(username, project_name):
#     p = Project.get_by(name=project_name)
#     if p is None:
#         print('create project: ', project_name)
#         p = Project(name=project_name, user=get_user(username))
#     return p


# def create(username, project_name):
#     project = get_project(username, project_name)
#     job = Job(jobid=create_jobid(username, project_name), project=project)
#     job.created_at = datetime.now()
#     print('Job:', job.jobid)


def create(user, project):
    job = Job(jobid=create_jobid(user, project), project=project, user=user)
    job.created_at = datetime.now()
    print('Job:', job.jobid)
    job.save()


def check():
    print('check  jobs')
    jobs = Job.query.filter(user='yarden').all()
    for j in jobs:
        print(j.jobid)

    print('check project')
    for j in Job.query.filter(project='foo').all():
        print('project ', j.jobid)


def test1():
    u1 = User(name='u1')
    u1.save()

    p11 = Project(name='p11', user=u1)
    p11.save()

    p12 = Project(name='p12', user=u1)
    p12.save()

    u = User.get_by(name='u1')
    print('u1:', u.name)

    user = User.get_by(name='u1')
    print('get by', user.name)

    p = Project.get_by(name='p11')
    print('p11:', p)

    p = Project.get_by(name='p12')
    print('p12:', p)

    p.delete()

    p = Project.get_by(name='p11')
    print('p11:', p)

    p = Project.get_by(name='p12')
    print('p12:', p)

    u1.delete()
    # users = User.query.filter(name='u1').all()
    # print('users:', users)

    p = Project.get_by(name='p11')
    print('p11:', p)

    p = Project.get_by(name='p12')
    print('p12:', p)


if __name__ == "__main__":
    run()
