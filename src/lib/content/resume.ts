export const resume = {
	languages: {
		fr: {
			education: [
				{
					name: 'Chalmers University of Technology',
					nameExplanation: 'Göteborg, Suède',
					startDate: 'Août 2020',
					endDate: 'Janvier 2021',
					title: 'Semestre d’échange académique',
					logo: 'chalmers.webp',
					description: [
						{
							mark: 'Réseaux de neurones artificiels',
							text: 'Réseau de neurones récurrents, Apprentissage supervisé/non supervisé/par renforcement, Machine Learning, Deep Learning, Python / Tensorflow / Keras.'
						},
						{
							mark: 'Architecture des ordinateurs',
							text: 'Architecture d’un processeur, MIPS assembleur, algorithme de Tomasulo, techniques d’optimisation, hiérarchie de mémoire, parallélisme et multiprocesseurs.'
						},
						{
							mark: 'Programmation fonctionnelle en Haskell',
							text: 'Structure de données, récursion, polymorphisme, tests, évaluation paresseuse, monades.'
						},
						{
							mark: 'Cryptographie',
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
					logo: 'isep.webp',
					description: [
						{
							mark: '3ème année',
							text: 'Projet d’algorithmique : Exploitation des données GTFS du réseau de transport de Rome ; Projet cybersécurité : attaques d’application web (XSS, CSRF, injection SQL, DoS/DDoS, flooding) ; Projet Web : plate- forme web, auth, chat (Architecture MVC, NodeJS, ReactJS, Redux, WebSock- ets, SQLite), méthodologie Agile, diagramme de Gantt/Pert, réalisations de tests unitaires ; Projet d’intelligence artificielle : analyse des premières don- nées sur le COVID-19, nettoyage, classification et estimation ; Participation à un projet de Tech for Good : personas, user story et maquettes pour le projet Chronic Buddy (association pour la mobilité des personnes atteintes de maladies chroniques).'
						},
						{
							mark: '2ème année',
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
							mark: 'Projet Personnel 1',
							text: 'Programme simulant le fonctionnement de la machine Enigma (en Python) et réalisation physique de celle-ci.'
						},
						{
							mark: 'Projet Personnel 2',
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
					logo: 'lvc.webp',
					description: null
				}
			],
			work: [
				{
					name: 'Chalmers University of Technology',
					nameExplanation: 'Göteborg, Suède',
					date: 'Août 2020',
					title: 'Semestre d’échange académique',
					description: [
						{
							mark: 'Réseaux de neurones artificiels',
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
			]
		},
		en: {
			education: [
				{
					name: 'Lycée de la Vallée de Chevreuse',
					nameExplanation: null,
					startDate: '2013',
					endDate: '2016',
					title:
						'Baccalauréat Scientifique (spécialité Mathématiques, Classe européenne, Mention Bien)',
					logo: 'lvc.webp',
					description: null
				}
			],
			work: [
				{
					name: 'Chalmers University of Technology',
					nameExplanation: 'Göteborg, Suède',
					date: 'Août 2020',
					title: 'Semestre d’échange académique',
					description: [
						{
							mark: 'Réseaux de neurones artificiels',
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
			]
		}
	}
} as const;

// export type ResumeType = typeof resume;
