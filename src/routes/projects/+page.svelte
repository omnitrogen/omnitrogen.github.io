<script lang="ts">
	import Card from '$lib/components/Card.svelte';
	import SimpleLayout from '$lib/components/SimpleLayout.svelte';
	import SocialIcons from '$lib/components/SocialIcons.svelte';
	import BriefcaseIcon from '$lib/assets/logos/briefcase-icon.svelte';

	const projects = [
		{
			name: 'Planetaria',
			description: 'Creating technology to empower civilians to explore space on their own terms.',
			link: { href: 'http://planetaria.tech', label: 'planetaria.tech' },
			logo: BriefcaseIcon
		},
		{
			name: 'Animaginary',
			description: 'High performance web animation library, hand-written in optimized WASM.',
			link: { href: '#', label: 'github.com' },
			logo: BriefcaseIcon
		},
		{
			name: 'HelioStream',
			description: 'Real-time video streaming library, optimized for interstellar transmission.',
			link: { href: '#', label: 'github.com' },
			logo: BriefcaseIcon
		},
		{
			name: 'cosmOS',
			description: 'The operating system that powers our Planetaria space shuttles.',
			link: { href: '#', label: 'github.com' },
			logo: BriefcaseIcon
		},
		{
			name: 'OpenShuttle',
			description:
				'The schematics for the first rocket I designed that successfully made it to orbit.',
			link: { href: '#', label: 'github.com' },
			logo: BriefcaseIcon
		}
	];
</script>

<svelte:head>
	<title>Projects - Félix Defrance</title>
	<meta name="description" content="Things I’ve made trying to put my dent in the universe." />
</svelte:head>
<SimpleLayout
	title="Things I’ve made trying to put my dent in the universe."
	intro="I’ve worked on tons of little projects over the years but these are the ones that I’m most proud of. Many of them are open-source, so if you see something that piques your interest, check out the code and contribute if you have ideas for how it can be improved."
>
	<ul role="list" class="grid grid-cols-1 gap-x-12 gap-y-16 sm:grid-cols-2 lg:grid-cols-3">
		{#each projects as project}
			<Card cardAs="li">
				<div
					class="relative z-10 flex h-12 w-12 items-center justify-center rounded-full bg-white shadow-md shadow-zinc-800/5 ring-1 ring-zinc-900/5 dark:border dark:border-zinc-700/50 dark:bg-zinc-800 dark:ring-0"
				>
					<project.logo />
				</div>
				<h2 class="mt-6 text-base font-semibold text-zinc-800 dark:text-zinc-100">
					<div
						class="absolute -inset-x-4 -inset-y-6 z-0 scale-95 bg-zinc-50 opacity-0 transition group-hover:scale-100 group-hover:opacity-100 sm:-inset-x-6 sm:rounded-2xl dark:bg-zinc-800/50"
					/>
					<a href={project.link.href}>
						<span class="absolute -inset-x-4 -inset-y-6 z-20 sm:-inset-x-6 sm:rounded-2xl" /><span
							class="relative z-10">{project.name}</span
						>
					</a>
				</h2>
				<Card Description>{project.description}</Card>
				<p
					class="relative z-10 mt-6 flex text-sm font-medium text-zinc-400 transition group-hover:text-teal-500 dark:text-zinc-200"
				>
					<SocialIcons Link class="h-6 w-6 flex-none" />
					<span class="ml-2">{project.link.label}</span>
				</p>
			</Card>
		{/each}
	</ul>
</SimpleLayout>
