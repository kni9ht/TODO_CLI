import click
import sys
import os
from datetime import date


@click.command()
@click.argument('option', default='help')
@click.argument('args', default='none')
def todo(option, args):
    todolist = list()

    if option == 'ls' and args == 'none':
        if os.path.exists('list.txt'):
            f = open('list.txt', 'r')
            lines = f.read()
            displayList = lines.split('\n')
            if len(displayList) > 1:
                displayList.pop(len(displayList)-1)
                count = 0
                for elem in displayList:
                    count = count + 1
                    print(f'[{count}] {elem}')
            else:
                print("Add somthing in the list")
        else:
            print('Add something to the list')

    elif option == 'add' and args != 'none':
        if not os.path.exists('list.txt'):
            f = open('list.txt', 'w')
            f.write('0')
            f.close()
        f = open('list.txt', 'r')
        lines = f.read()
        lisst = lines.split('\n')
        lisst.insert((len(lisst)-1), args)
        notes = '\n'.join(str(elem) for elem in lisst)
        f.close()
        f = open('list.txt', 'w')
        f.write(notes)
        f.close()
        print(f'Added todo : "{args}"')

    elif option == 'help' and args == 'none':
        print("Usage :-")
        print("$ ./todo add 'todo item'  # Add a new todo")
        print("$ ./todo ls               # Show remaining todos")
        print("$ ./todo del NUMBER       # Delete a todo")
        print("$ ./todo done NUMBER      # Complete a todo")
        print("$ ./todo help             # Show usage")
        print("$ ./todo report           # Statistics")

    elif option == 'del' and args != 'none':
        if os.path.exists('list.txt'):
            f = open('list.txt', 'r')
            args = int(args)
            args = args-1
            lines = f.read()
            todolist = lines.split('\n')
            if len(todolist) > 1:
                todolist.pop(args)
                f.close()
                f = open('list.txt', 'w')
                lisst = '\n'.join([str(elem) for elem in todolist])
                f.write(lisst)
                print(f'Deleted todo #{args+1}')
            else:
                print("NOthing to delete !")
        else:
            print("You may have accidently deleted the database")

    elif option == 'done' and args != 'none':
        if os.path.exists('list.txt'):
            f = open('list.txt', 'r')
            args = int(args)
            args = args-1
            lines = f.read()
            todolist = lines.split('\n')
            # todolist.pop(len(todolist)-1)
            todolist.pop(args)
            done = todolist[len(todolist) - 1]
            todolist.pop(len(todolist)-1)
            done = int(done)
            done = done+1
            todolist.append(done)
            # todolist.append('\n')
            f.close()
            f = open('list.txt', 'w')
            lisst = '\n'.join([str(elem) for elem in todolist])
            f.write(lisst)
        else:
            print("You may have accidently deleted the database")

    elif option == 'report' and args == 'none':
        if os.path.exists('list.txt'):
            f = open('list.txt', 'r')
            lines = f.read()
            lisst = lines.split('\n')
            # lisst.pop(len(lisst)-1)
            done = int(lisst[len(lisst)-1])
            pending = int(len(lisst)-1)
            print(f'{date.today()} PENDING : {pending} COMPLETED : {done}')
        else:
            print(f'{date.today()} Add somthing to list to generate report')

    else:
        print("Something went wrong ..! Please goto help")


if __name__ == '__main__':
    todo()
