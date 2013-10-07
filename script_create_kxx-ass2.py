from render import *
if __name__ == "__main__":
    nav = NavBar()
    nav.addLink(Home="index.html")
    nav.addLink(Introduction="intro.html")
    nav.addLink(Audience="aud.html")
    nav.addLink(Design="design.html")
    #nav.addLink(Resources="resources.html")
    nav.addLink(Register="register.html")

    student = Student(name="Lu Zhe Xuan", id="174047", email="xxxx@xx.com", course="KXX133 web management ass2")

    # Base page
    basePage = Page(tpl="base.mako", title='Wild world', subtitle='Mammals of Tasmania', student=student)
    basePage.addCSS('main.css')
    basePage.addJS(MAIN_JS)
    basePage.addNav(nav)

    # Intro page
    page = basePage.duplicated()
    post = Post(title="", content=readContent("kxx-ass2", "animals.txt"))
    page.addPost(post)

    post = Post(title="Animals", content="This animal has extremely strong front limbs and claws due to its mechanical advantage which allows it to burrow quickly with great power. As it needs to be able to survive underground it has a significant tolerance to high levels of carbon dioxide and low levels of oxygen. It has no weapons or fighting ability but repels predators by curling into a ball and deterring them with its spines. The animal lacks the ability to sweat and cannot deal with heat well so it tends to avoid daytime activity in hot weather. It can swim if needed. The snout has mechanical and electroreceptors that help the echidna to detect what is around it.")
    post.addImage("animal_x_1.jpg", width=300)
    page.addPost(post)
    post = Post(title="Animals", content="This animal are sturdy and built close to the ground. When fully grown, they can reach between 80 and 130 cm, and weigh between 17 and 40 kg. The wombats found on Tasmania and Flinders Island are often smaller than their mainland counterparts. It is distinguished from both hairy-nosed wombats by its bald nose.")
    post.addImage("animal_x_2.jpg", width=300)
    page.addPost(post)
    post = Post(title="Animals", content="This animal have large, powerful hind legs, large feet adapted for leaping, a long muscular tail for balance, and a small head. Like most marsupials, female have a pouch called a marsupium in which joeys complete postnatal development.")
    post.addImage("animal_x_3.jpg", width=300)
    page.addPost(post)

    page.render("intro.html")

    # Index page
    page2 = basePage.duplicated()
    page2.addJS("slider.js")
    introPost = Post(title="Welcome to the animals world", content=readContent("kxx-ass2",  "flow_pictures.txt"))
    page2.addPost(introPost)
    page2.render("index.html")


   # audience
    page3 = basePage.duplicated()
    audPost = Post(title="Audience", content=readContent("kxx-ass2", "aud.txt"))
    page3.addPost(audPost)
    page3.render("aud.html")

    # design page
    page4 =  basePage.duplicated()
    designPost = Post(title="Design", content=readContent("kxx-ass2", "design.txt"))
    page4.addPost(designPost)
    page4.render( "design.html")

    # resource page
    page5 = basePage.duplicated()
    p = Post(title="Resources", content=readContent("kxx-ass2", "resource.txt"))
    page5.addPost(p)
    #page5.render("resources.html")


   # Register page
    page6 = basePage.duplicated()
    p = Post(title="Register", content=readContent("kxx-ass2", "register.txt"))
    page6.addPost(p)
    page6.render("register.html")