import chalmers from '$lib/assets/images/chalmers.webp';
import hello_watt from '$lib/assets/images/hello-watt.png';
import irt_systemx from '$lib/assets/images/irt-systemx.png';
import isep from '$lib/assets/images/isep.webp';
import lvc from '$lib/assets/images/lvc.webp';
import mnhn from '$lib/assets/images/mnhn.png';
import partoo from '$lib/assets/images/partoo.png';

export const resume = {
	languages: {
		fr: {
			work: [
				{
					name: 'MNHN',
					nameExplanation: "Muséum national d'Histoire naturelle",
					date: '2022 - 2025 (3 ans)',
					title: 'Développeur mobile',
					logo: mnhn,
					description: [
						{
							title: null,
							text: 'INPN Espèces...'
						}
					],
					stack: ['Flutter']
				},
				{
					name: 'IRT SystemX',
					nameExplanation: 'Accélérateur de la transformation numérique des territoires',
					date: '2021 (6 mois)',
					title: 'Stage data science et web full-stack',
					logo: irt_systemx,
					description: [
						{
							title: null,
							text: 'Analyse, intégration et exploitation des données dans le cadre d’une application interactive pour la planification énergétique territoriale'
						}
					],
					stack: [
						'React',
						'Redux',
						'Redux Saga',
						'Mapbox GL',
						'Azure Fonctions (NodeJS)',
						'Cosmos DB',
						'Data Explorer',
						'Digital Twins',
						'Static Web App',
						'PostgreSQL',
						'Python',
						'Github Actions CI/CD'
					]
				},
				{
					name: 'Hello Watt',
					nameExplanation: 'Conseiller énergie du particulier',
					date: '2019 (6 mois)',
					title: 'Stage R&D développeur full-stack',
					logo: hello_watt,
					description: [
						{
							title: null,
							text: 'Participation à la conception et au développement de la plateforme de diagnostic énergétique, optimisations SEO (structured data)'
						}
					],
					stack: [
						'Django',
						'React',
						'AWS Elastic Beanstalk',
						'AWS Lambda',
						'AWS S3',
						'AWS Cloudwatch',
						'MySQL',
						'mongoDB'
					]
				},
				{
					name: 'Hackathons',
					nameExplanation: null,
					date: 'Depuis 2017',
					title: 'Membre de l’équipe de hackathon de l’ISEP',
					logo: isep,
					description: [
						{
							title: null,
							text: 'Participation à plusieurs compétitions : IEEE Xtreme (185ème équipe mondiale, 3ème équipe française), Battle dev (400ème sur 3000), Nuit de l’info (1er prix pour le challenge de récupération et traitement de données de satellites géospaciaux), Hackathon Vivatech.'
						},
						{
							title: null,
							text: 'Participation au FOSDEM depuis 2019 (Free and Open source Software Developers’ European Meeting).'
						}
					],
					stack: null
				},
				{
					name: 'Partoo',
					nameExplanation: 'Amélioration de la visibilité sur internet',
					date: '2017 (1 mois)',
					title: 'Stage R&D',
					logo: partoo,
					description: [
						{
							title: null,
							text: 'Réalisation d’une interface web interne pour faciliter la récupération de fichiers clients par les "customer success" dans la base de données.'
						}
					],
					stack: ['Pyramid (Python)', 'Javascript', 'MongoDB', 'Redis']
				}
			],
			education: [
				{
					name: 'Chalmers University of Technology',
					nameExplanation: 'Göteborg, Suède',
					startDate: 'Août 2020',
					endDate: 'Janvier 2021',
					title: 'Semestre d’échange académique',
					logo: chalmers,
					description: [
						{
							title: 'Réseaux de neurones artificiels',
							text: 'Réseau de neurones récurrents, Apprentissage supervisé/non supervisé/par renforcement, Machine Learning, Deep Learning, Python / Tensorflow / Keras.'
						},
						{
							title: 'Architecture des ordinateurs',
							text: 'Architecture d’un processeur, MIPS assembleur, algorithme de Tomasulo, techniques d’optimisation, hiérarchie de mémoire, parallélisme et multiprocesseurs.'
						},
						{
							title: 'Programmation fonctionnelle en Haskell',
							text: 'Structure de données, récursion, polymorphisme, tests, évaluation paresseuse, monades.'
						},
						{
							title: 'Cryptographie',
							text: 'Cryptographie symétrique, chiffrement de flux/par bloc, cryptographie asymétrique (RSA, ElGamal), infrastructure à clés publiques, théorie des nombres/des groupes, attaques et vulnérabilités des protocoles.'
						}
					]
				},
				{
					name: 'ISEP',
					nameExplanation: 'Institut Supérieur d’Electronique de Paris',
					startDate: '2018',
					endDate: '2021',
					title: 'Cycle ingénieur spécialisation Logiciel',
					logo: isep,
					description: [
						{
							title: '3ème année',
							text: 'Projet d’algorithmique : Exploitation des données GTFS du réseau de transport de Rome ; Projet cybersécurité : attaques d’application web (XSS, CSRF, injection SQL, DoS/DDoS, flooding) ; Projet Web : plate- forme web, auth, chat (Architecture MVC, NodeJS, ReactJS, Redux, WebSock- ets, SQLite), méthodologie Agile, diagramme de Gantt/Pert, réalisations de tests unitaires ; Projet d’intelligence artificielle : analyse des premières don- nées sur le COVID-19, nettoyage, classification et estimation ; Participation à un projet de Tech for Good : personas, user story et maquettes pour le projet Chronic Buddy (association pour la mobilité des personnes atteintes de maladies chroniques).'
						},
						{
							title: '2ème année',
							text: 'Projet domotique : Site de gestion d’une maison (HTML, CSS, JS, PHP), et de capteurs (carte TI) sécurisés par une clé sonore (filtrage, traitement du signal à l’aide de MATLAB) ; Jeu KingDomino en Java.'
						}
					]
				},
				{
					name: 'ISEP',
					nameExplanation: 'Institut Supérieur d’Electronique de Paris',
					startDate: '2016',
					endDate: '2018',
					title: 'Cycle préparatoire associé MPSI puis PSI',
					logo: 'isep.webp',
					description: [
						{
							title: 'Projet Personnel 1',
							text: 'Programme simulant le fonctionnement de la machine Enigma (en Python) et réalisation physique de celle-ci.'
						},
						{
							title: 'Projet Personnel 2',
							text: 'Machine résolvant le Rubik’s cube (en Python pour l’interface et la reconnaissance d’image, et en Arduino pour le contrôle des moteurs).'
						}
					]
				},
				{
					name: 'Lycée de la Vallée de Chevreuse',
					nameExplanation: null,
					startDate: '2013',
					endDate: '2016',
					title:
						'Baccalauréat Scientifique (spécialité Mathématiques, Classe européenne, Mention Bien)',
					logo: lvc,
					description: null
				}
			]
		},
		en: {
			work: [
				{
					name: 'Chalmers University of Technology',
					nameExplanation: 'Göteborg, Suède',
					date: 'Août 2020',
					title: 'Semestre d’échange académique',
					logo: chalmers,
					description: [
						{
							title: 'Réseaux de neurones artificiels',
							text: 'Réseau de neurones récurrents, Apprentissage supervisé/non supervisé/par renforcement, Machine Learning, Deep Learning, Python / Tensorflow / Keras.'
						}
					],
					stack: [
						{
							name: '',
							logo: null,
							color: null
						}
					]
				}
			],
			education: [
				{
					name: 'Lycée de la Vallée de Chevreuse',
					nameExplanation: null,
					startDate: '2013',
					endDate: '2016',
					title:
						'Baccalauréat Scientifique (spécialité Mathématiques, Classe européenne, Mention Bien)',
					logo: lvc,
					description: null
				}
			]
		}
	}
} as const;
