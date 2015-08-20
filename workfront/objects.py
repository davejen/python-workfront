from .generated_objects import *


class Issue(Issue):

    def convert_to_task(self):
        data = self.session.put(
            self.api_url()+'/convertToTask',
            params=dict(
                updates=dict(
                    options=['preserveIssue',
                             'preservePrimaryContact',
                             'preserveUpdates'],
                    task=dict(name=self.name,
                              description=self.description,
                              enteredByID=self.entered_by_id,
                              )
            )))
        return Task(self.session, ID=data['result'])


class Update(Update):

    @property
    def update_obj(self):
        return Object.from_data(self.session, dict(ID=self.update_obj_id,
                                                   objCode=self.update_obj_code))