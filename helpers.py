from faker import Faker


class UserData:

    @staticmethod
    def create_user_data():
        faker = Faker()
        user_data = {"email": faker.email(),
                    "password": faker.password(),
                    "name": faker.first_name()
                     }
        return user_data

    @staticmethod
    def create_user_no_name():
        faker = Faker()
        user_data_no_name = {"email": faker.email(),
                            "password": faker.password()
                             }
        return user_data_no_name

    @staticmethod
    def create_user_no_password():
        faker = Faker()
        user_data_no_password ={"email": faker.email(),
                               "name": faker.first_name()
                                }
        return user_data_no_password

    @staticmethod
    def create_user_no_email():
        faker = Faker()
        user_data_no_email = {"password": faker.password(),
                             "name": faker.first_name()
                              }
        return user_data_no_email