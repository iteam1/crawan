### project's goals

The table below give you full description about this project. Click on goal's name for going to detail.

|No|Goal|Brief|
|---|---|---|
|01|[user's experiences](#user's-experiences)|let the user can easily do some with the source code, and gain something special|
|02|[os system](#os-system)|`crawan` can be run on varitety of os-system|
|03|[new](#new)|`crawan` have to catch up and be able to work in the future|
|04|[easy to initialize](#easy-to-initialize)|the best structure is now not exist, let make a strategy to release some quickly and easily|
|05|[adaptation](#adaptation)|duel to the GUI changing, `crawan` must be structure to adapt this|

#### user's experiences
there are a lot of level of user (also developer or coder etc.). let classify them into 3 kinds:
- **beginner:** `crawan` can give them gain some by just few command as `git clone`, `bash` or `python [run-something]`. we named the scraping-script is `run.py` for all.
- **advancer:** they can modify source code follow their own desires, reuse some module,etc.
- **professional:** they can contribute their ideas, make it stronger and bigger.

#### os-system
`linux`,`windows`,`mac` are 3 popular os system in the world, so building `crawan` must be orientated from the begining for these changes.
`crawan` was developed on 2 os-system `windows7` and `ubuntu18.04` each os-system have a different dependencies for installing requirements, you can run `pip install -r windows-requirements.txt` on windows or `pip3 install -r ubuntu-requirements.txt` or create your own virtual environment and install it manually

#### new
new web-browser every year, even the project's packages and dependencies release new verion every year, so building `crawan` must be orientated from the begining for these changes.

#### easy to initialize
create a main theme branch, create some developing branch base on `main-branch template` but customize the structure follow your implementation until you find the best option. it may be time-wasting but give you some quick demo

#### adaptation
website gui change every day, they have some solution to anti crawling, you have to structure your source by module, don't let the small change can make your code crash. the more you seperate into module, the more you can easily to maintain and rebuild it. follow this [UML](). 
