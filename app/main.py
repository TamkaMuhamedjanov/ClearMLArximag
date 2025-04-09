from decorators import TaskDecorator

@TaskDecorator.cml_task(yaml_file='/Users/xochuhalal/Downloads/DistributedComputingSystemClearML-main/app/decorators/testConfig.yaml')
def example_function():
    print("Task is running...")


# Вызов функции
example_function()

