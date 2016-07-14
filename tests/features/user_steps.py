# -*- coding: utf-8 -*-
from lettuce import step
from helpers.injectors import UserInjector
from helpers.generators import PasswordGenerator

@step(u'Given I\'ve added the user "([^"]*)"')
def given_i_ve_added_the_user_group1(step, group1):
    injector = UserInjector()
    pass_generator = PasswordGenerator()
    injector.create_new(group1[0], pass_generator.create_new(), group1[1], group1[2])


@step(u'When I go to the user list in the Admin application')
def when_i_go_to_the_user_list_in_the_admin_application(step):
    assert False, 'This step must be implemented'

@step(u'Then I should find the name "([^"]*)", admin role "([^"]*)" and active state "([^"]*)"')
def then_i_should_find_the_name_group1_admin_role_group2_and_active_state_group3(step, group1, group2, group3):
    assert False, 'This step must be implemented'
