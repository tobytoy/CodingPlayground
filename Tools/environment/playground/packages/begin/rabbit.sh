#! /bin/sh                                                                                                                                                                                    

rabbitmqctl add_user toby 1234
rabbitmqctl set_user_tags toby administrator
rabbitmqctl set_permissions -p / toby ".*" ".*" ".*"
rabbitmqctl  delete_user guest
