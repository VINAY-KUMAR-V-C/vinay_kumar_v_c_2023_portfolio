from django.shortcuts import render,HttpResponse,redirect

class CompleteInfo():
    def getCompleteInfo(self) -> str:
        return {
        'profile': {
            'name': 'Vinay Kumar V C',
            'company': {
                'name': 'PayPal',
                'role': {
                    'name':'Software Engineer',
                    'link':'https://www.google.com/search?q=Software+Engineer'
                },  
                'link': 'https://www.google.com/search?q=PayPal'
            },
            'location': {
                'name': 'Bengaluru, Karnataka',
                'link': 'https://www.google.com/maps/place/Bangalore%2C%20Karnataka',
            },
            'description': 'Software Engineer @ PayPal',
            'CVLink':'static/image/VinayKumarVC.pdf',
            'profilePhoto':{
                'fromStatic' : 'static/image/IMG_2907.jpg',
                'fromRepo' : 'https://avatars.githubusercontent.com/u/84114504?v=4'
            }
        },
        'contactInfo': {
            'linkedin': {
                'name': 'linkedIn',
                'link': 'https://www.linkedin.com/in/VinayKumarVC/'
            },
            'facebook': {
                'name': 'facebook',
                'link': 'value'
            },
            'github': {
                'name': 'github',
                'link': 'https://github.com/VINAY-KUMAR-V-C'
            },
            'twitter': {
                'name': 'twitter',
                'link': 'value'
            },
            'skype': {
                'name': 'skype',
                'link': 'value'
            },
            'instagram': {
                'name': 'instagram',
                'link': 'https://instagram.com/vinay_kumar_v_c?igshid=MWRsd2sweThldnl0Yg%3D%3D&utm_source=qr'
            },
            'leetCode': {
                'name': 'leetCode',
                'link': 'https://leetcode.com/VINAY_KUMAR_V_C/'
            }
        },
        'details': {
            'experience': {
                'name': 'experience',
                'value': [
                    {
                        'name': 'PayPal',
                        'startEnd': '15/12/2025 - Current',
                        'location': 'Chennai',
                        'role': 'Software Engineer',
                        'projects': 
                            {
                                'name': [],
                                'technologies': []
                            }
                    },
                    {
                        'name': 'Zoho CRM',
                        'startEnd': '17/08/2022 - 10/12/2025',
                        'location': 'Chennai',
                        'role': 'Software Developer (MTS)',
                        'projects': 
                            {
                                'name': ['Developed rich text field support', 'Worked on formula fields and notes module enchanments','Completed handling for coverting multiline to rich text fields'],
                                'technologies': ['Java','Spring', 'JS', 'Python', 'CSS','PSQL','MySQL']
                            }
                    },
                    {
                        'name': '10 Seconds (Internship)',
                        'startEnd': '10/10/2021 - 08/02/2022',
                        'location': 'Remote',
                        'role': 'Project Trainee',
                        'projects':
                            {
                                'name': ['Developed portfolio website'],
                                'technologies': ['Python','Django', 'Flask', 'MySQL', 'JS']
                            }
                    }
                ]
            },
            'education': {
                'name': 'education',
                'value': [
                    {
                        'name': 'SKSJTI Engineering College',
                        'startEnd': '05/08/2018 - 15/07/2022',
                        'location': 'Bengaluru',
                        'branch': 'Computer Science',
                        'course': 'Graducation - B.Tech/BE'
                    },
                    {
                        'name': 'Vidya Kirana PU College',
                        'startEnd': '10/07/2016 - 01/05/2018',
                        'location': 'Bengaluru',
                        'course': 'Class XII / Intermediate'
                    },
                    {
                        'name': 'BLOSSOMS School',
                        'startEnd': '4/05/2015 - 15/05/2016',
                        'location': 'Bengaluru',
                        'course': 'Class X / SSLC'
                    }
                ]
            },
            'skills': [
                {
                    'name': 'Frontend',
                    'value': ['JavaScript', 'HTML', 'CSS', 'Bootstrap(basics)']
                },
                {
                    'name': 'Backend',
                    'value': ['Flask', 'Django', 'Struts', 'Spring Boot(Learning)']
                },
                {
                    'name': 'Programming Languages',
                    'value': ['JavaScript', 'C++(Learning)', 'Python', 'Java', 'C']
                },
                {
                    'name': 'JavaScript Libraries',
                    'value': ['Axios','AJAX','ASYNC-AWAIT','etc...']
                },
            ],
            'projects': [
                {
                    'name': 'A CRUD app with session management.',
                    'technologies': ['NodeJS', 'Express', 'PSQL/pg', 'ejs', 'SQL', 'etc...'],
                    'repo': [
                        {
                            'name': 'VAV_IT_IS',
                            'link': 'https://github.com/VINAY-KUMAR-V-C/VAV_IT_IS'
                        }
                    ],
                    'deployment': {
                        'name': 'https://vav-it-is.vercel.app/',
                        'link': 'https://vav-it-is.vercel.app/'
                    }
                },
                {
                    'name': 'Data science based online yoga trainer',
                    'technologies': ['Python', 'Flask', 'HTML', 'JS', 'SQL', 'etc...'],
                    'repo': [
                        {
                            'name': 'Final year project',
                            'link': 'https://github.com/VINAY-KUMAR-V-C/BE_projects/tree/master/FINAL%20YEAR%20PROJECT%20VINAY'
                        }
                    ],
                    'deployment': {
                        'name': 'Local host project',
                        'link': None
                    }
                },
                {
                    'name': 'Portfolio',
                    'technologies': ['Django', 'Flask', 'PSQL', 'JS', 'SQL', 'Python', 'etc...'],
                    'repo': [
                        {
                            'name': 'Portfolio using Django',
                            'link': 'https://github.com/VINAY-KUMAR-V-C/portfolioUsingDjango'
                        },
                        {
                            'name': 'Portfolio using Flask',
                            'link': 'https://github.com/VINAY-KUMAR-V-C/BE_projects/tree/master/portfolio'
                        }
                    ],
                    'deployment': {
                        'name': 'https://vinay-kumar-v-c.vercel.app/resume/',
                        'link': 'https://vinay-kumar-v-c.vercel.app/resume/'
                    }
                },
                {
                    'name': 'Library Management System',
                    'technologies': ['MySQL', 'HTML', 'CSS', 'JS', 'PHP'],
                    'repo': [
                        {
                            'name': 'DBMS project',
                            'link': 'https://github.com/VINAY-KUMAR-V-C/BE_projects/tree/master/DBMS%20project/minproject-3'
                        }
                    ],
                    'deployment': {
                        'name': 'Local host project',
                        'link': None
                    }
                }
            ]
        },
    }

def getDetails(request,unmatched_path):
    if unmatched_path=='details':
        return render(request, 'details.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
    elif unmatched_path=='experience':
        return render(request,'experience.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
    elif unmatched_path=='education':
        return render(request,'education.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
    elif unmatched_path=='projects':
        return render(request,'projects.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
    elif unmatched_path=='skills':
        return render(request,'skills.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
    return render(request,'PageNotFound404.html')

def home(request):
    return render(request, 'home.html',{'completeInfo':CompleteInfo().getCompleteInfo()})
