<script lang="ts">
	import Container from './Container.svelte';

	export let title: string;
	export let intro: string;
</script>

<Container classStr="mt-16 sm:mt-32">
	<header class="max-w-2xl">
		<h1 class="text-4xl font-bold tracking-tight text-zinc-800 sm:text-5xl dark:text-zinc-100">
			{title}
		</h1>
		<p class="mt-6 text-base text-zinc-600 dark:text-zinc-400">
			{intro}
		</p>
	</header>
	<div class="mt-16 sm:mt-20"><slot /></div>
</Container>
