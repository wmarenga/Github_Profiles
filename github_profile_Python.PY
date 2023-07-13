class PythonDataAnalyst:
    def __init__(self):
        self.name = "Hello World! I'm Wellington Marenga Junior."
        self.aboutme = "I'am passionate about technology and fascinated to be a part of, like a tiny neuron, this complex new world that will change the world forever. With my ethics and evolutionary mindset, I intend to use my skill set to ensure relevant information that guide us to a better world."
        self.goal = "My goal is to use data analysis to find answers to society's demands."
        self.learning = "I'm currently learning Hadoop and Big Data."
        self.challenge = "I'm currently looking for challenging projects in data analysis."
        self.collaboration = "I'm looking to collaborate on data science projects."
        self.askme = "Ask me about Python, Power BI and SQL."
        self.email = "How to reach me (wmarenga44@gmail.com)."
        self.career = "Find out more about my professional career on linkedIn."
        self.cv = "Know about my experiences"

    def say_hi(self):
        print(f'{self.name} 👋')
        print(f'{self.aboutme}')
        print(f'- 🎯 {self.goal}')
        print(f'- 💡 {self.learning}')
        print(f'- 🌱 {self.challenge}')
        print(f'- 🦾 {self.collaboration}')
        print(f'- 🥁 {self.askme}')
        print(f'- 📩 {self.email}')
        print(f'- 👣 {self.career}')
        print(f'- ✅ {self.cv}')
        print("Thanks for dropping by!")


me = PythonDataAnalyst()
me.say_hi()
