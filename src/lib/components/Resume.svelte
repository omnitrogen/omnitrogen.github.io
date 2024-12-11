<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import BriefcaseIcon from '$lib/assets/logos/briefcase-icon.svelte';
	import type { Component } from 'svelte';

	interface Role {
		company: string;
		title: string;
		logo: Component;
		start: string;
		end: string;
	}

	// This could be fetched from an API or passed as props as shown here
	let resume: Role[] = [
		{
			company: 'Planetaria',
			title: 'CEO',
			logo: BriefcaseIcon, // Replace with the actual path to your logo file
			start: '2019',
			end: 'Present'
		},
		{
			company: 'Airbnb',
			title: 'Product Designer',
			logo: BriefcaseIcon, // Replace with the actual path to your logo file
			start: '2014',
			end: '2019'
		},
		{
			company: 'Facebook',
			title: 'iOS Software Engineer',
			logo: BriefcaseIcon, // Replace with the actual path to your logo file
			start: '2011',
			end: '2014'
		},
		{
			company: 'Starbucks',
			title: 'Shift Supervisor',
			logo: BriefcaseIcon, // Replace with the actual path to your logo file
			start: '2008',
			end: '2011'
		}
	];
</script>

<div class="rounded-2xl border border-zinc-100 p-6 dark:border-zinc-700/40">
	<h2 class="flex text-sm font-semibold text-zinc-900 dark:text-zinc-100">
		<BriefcaseIcon />
		<span class="ml-3">Work</span>
	</h2>
	<ol class="mt-6 space-y-4">
		{#each resume as role}
			<li class="flex gap-4">
				<div
					class="relative mt-1 flex h-10 w-10 flex-none items-center justify-center rounded-full shadow-md shadow-zinc-800/5 ring-1 ring-zinc-900/5 dark:border dark:border-zinc-700/50 dark:bg-zinc-800 dark:ring-0"
				>
					<role.logo />
				</div>
				<dl class="flex flex-auto flex-wrap gap-x-2">
					<dt class="sr-only">Company</dt>
					<dd class="w-full flex-none text-sm font-medium text-zinc-900 dark:text-zinc-100">
						{role.company}
					</dd>
					<dt class="sr-only">Role</dt>
					<dd class="text-xs text-zinc-500 dark:text-zinc-400">
						{role.title}
					</dd>
					<dt class="sr-only">Date</dt>
					<dd
						class="ml-auto text-xs text-zinc-400 dark:text-zinc-500"
						aria-label={`${role.start} until ${role.end}`}
					>
						<time>
							{role.start}
						</time>{' '}
						<span aria-hidden="true">—</span>{' '}
						<time>
							{role.end}
						</time>
					</dd>
				</dl>
			</li>
		{/each}
	</ol>
	<Button href="#" variant="secondary" classStr="group mt-6 w-full">Download CV</Button>
</div>
