# Internship kickoff repo

This repo serves as test environment for github features, mainly **Basic Actions *(clone, pull, push, branches...)***, **Pull Requests & Merges**, **Tickets** and **Security**.

The main branch is locked by a security rule to only allow Admin to push/merge code. As a **Team**, you should **NOT** be working on main branches, but rather create your own branch, do your coding, and submit for a pull request. 
This will allow the repo admin(s) to review your code, suggest some changes and finally merge your code into production.

## How it works
### 1. Pull requests - *[video demo](https://www.youtube.com/watch?v=MnUd31TvBoU)*
First thing first, you need to clone this repository to be able to work on it
```sh
git clone https://github.com/CraftSchoolship/internship.git
cd sandbox
```
If you already cloned this repo and some changes have added to it after you cloned it then you can use
```sh
git checkout main
git pull origin main
```
After that, you need to create a new branch to work with. The new branch name should be unique and not in use, and for standardisation purposes the name is better be related to a *Ticket*
> For more about tickets scroll down to [Issues & Tickets](#issues_and_tickets)
```sh
git checkout -b NEW_BRANCH_NAME
```
Now you can write and edit whatever code/files you want, and once you're done and ready to push them up, use
```sh
git add .
git commit -m "YOUR_COMMIT_MESSAGE_HERE"
git push -u origin NEW_BRANCH_NAME
```
And now your code is in the GitHub repo, you can submit for a **Pull Request**
1. Open your GitHub repo in your browser
2. You should find your last pushed branche with a button labeled `Compare & Pull Request`, click on that button
3. You'll be redirected to a new page titeled *Open a pull request*, fill in your description and click on `Create Pull Request`
4. On this phase your pull request is created, Now wait for an admin to *Review* and *Comment* your code
  + You may be requested to add some adjustments to your code, or
  + Your pull request may be approved and merged to main branch


### 2. Issues and Tickets - *[video demo](https://www.youtube.com/watch?v=bDqaIAOSUp4)*
This section is still under construction... You can watch the *video demo* instead

## How to document code
### 1. README.md file
Writing README.md files is usually related to repos or modules, and while working with code snippets you may not be required to add this file often, but nonetheless, you're still required to know how to write a clean one when requested.

Of course, before even starting you're reduired to know **Markdown Syntaxe**, if you don't, here are some references to get started
+ [Markdown Docs for Beginners](https://www.markdownguide.org/getting-started/)
+ [Markdown Editor](https://readme.so/editor)

A default README.md file layout should look as the following *(NOTE: `<!-- ... -->` are comments)*
```md
# Your Repo/Module Title
![version 1.0](https://img.shields.io/badge/version-1.0-blue)
<!-- The first one is the current Repo/Module version, Repeat this also for all major dependancies, i.e AWS, Python, Helm, Java... -->

Then write a description for the repo/module, what it's, what is it used for,...

### :bangbang: Important
+ List Your
+ Important Notes
+ If exists

### Content
Describe a tree hierarchy of content if it's important to know, skip this part if the content is standardly organized, not interessting to know or the content is too large and complex
Here's how to write a tree
\```bash
.
├── File
├── Folder1
|   ├── File11
|   └── File12
└── Folder2
    ├── File21
    └── File22
\```

### Usage
If you're code is executable or installable then provide the instructions to do so, i.e
\```bash
mkdir test
cd test
echo "hello world from test"
\```

### Values/Variables/Defaults
If you're code use env vars, allows customization or require some entries, provide them in this section, best approach is to use a Table
| Name | Type | Default Value | Description |
| --- | --- | --- | --- |
| Var1 | String | "hello" | my var1 desc |
| Var2 | int | 0 | my var2 desc |
```

### 2. Code Comment Docs
One important key Code Docs is **Comments**. Each programming language has standardized a way to write comments that enables *IDEs*, *code editors* and *other programmers* to understand what a block of code do. 

In this section, we'll only focus on documenting *Functions* & *Methods*, but keep inn mind that other blocks of code have to be documented too *(i.e classes, complex instructions, special notes...)
##### Python Docs *[Guide](https://realpython.com/documenting-python-code)*
```py
def myFunction(param1:type, param2,type=VALUE):type
    """Lorem ipsum dolor sit amet consectetur adipisicing elit.

    Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat vero tempora 
    asperiores. Molestias vel corrupti ipsum libero blanditiis nulla non, distinctio 
    architecto laborum commodi earum qui voluptate enim nisi alias!

    Parameters
    ----------
    param1 : type
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
    param2 : type, optional
        Lorem ipsum dolor sit amet consectetur adipisicing elit. (default is VALUE)

    Returns
    -------
    type
        Lorem ipsum dolor sit amet consectetur adipisicing elit.

    Raises
    -------
    ErrorType
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
    """

    # code starts here
```
##### Java Docs
```java
/**
 * <h1> Function Label </h>
 * 
 * <p>
 * Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat vero tempora 
 * asperiores. Molestias vel corrupti ipsum libero blanditiis nulla non, distinctio 
 * architecto laborum commodi earum qui voluptate enim nisi alias!
 * </p>
 * 
 * @param  param1  Lorem ipsum dolor sit amet consectetur adipisicing elit.
 * @param  param2  Lorem ipsum dolor sit amet consectetur adipisicing elit.
 * @return         Molestias vel corrupti ipsum libero blanditiis nulla non.
 * @throws         Thrown Exceptions if any
 * @see            Reference for other methods if any
 */
public Type myFunction(Type param1, Type param2) {
    // code starts here
}
```
