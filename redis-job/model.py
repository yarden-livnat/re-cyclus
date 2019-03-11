import rom
from rom.util import IDENTITY
#
# class User(rom.Model):
#     name = rom.Text(required=True, unique=True)
#     projects = rom.OneToMany('Project')
#
#
# class Project(rom.Model):
#     name = rom.Text(required=True, unique=True)
#     user = rom.ManyToOne('User', 'cascade')
#     job = rom.OneToMany('Job')


class Job(rom.Model):
    jobid = rom.Text(required=True, unique=True, index=True, keygen=IDENTITY)
    user = rom.Text(required=True, index=True, keygen=IDENTITY)
    project = rom.Text(required=True, index=True, keygen=IDENTITY)
    tasks = rom.OneToMany('Task')
    status = rom.Text(default='created')
    created_at = rom.DateTime()
    completed_at = rom.DateTime()


class Task(rom.Model):
    name = rom.Text(required=True, unique=True)
    job = rom.OneToMany('Job')
    create_at: rom.DateTime()
    completed_at: rom.DateTime()
    type: rom.Text()
    parms: rom.Json()
