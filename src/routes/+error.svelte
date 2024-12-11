<script lang="ts">
	import { page } from '$app/stores';
	import Container from '$lib/components/Container.svelte';
	import { onMount } from 'svelte';
	import Layout from './+layout.svelte';

	onMount(() => {
		document.body.classList.remove('flex-col');
		return () => {
			document.body.classList.add('flex-col');
		};
	});
</script>

{#if $page.error?.message === 'Not Found'}
	<Container classStr="flex h-full items-center pt-16 sm:pt-32">
		<div class="flex flex-col items-center">
			<p class="text-base font-semibold text-zinc-400 dark:text-zinc-500">404</p>
			<span class="mt-4 text-4xl">🕳</span>
			<h1
				class="mt-4 text-4xl font-bold tracking-tight text-zinc-800 sm:text-5xl dark:text-zinc-100"
			>
				Page not found
			</h1>
			<p class="mt-4 text-base text-zinc-600 dark:text-zinc-400">
				Sorry, we couldn’t find the page you’re looking for.
			</p>
			<a
				class="mt-4 inline-flex items-center justify-center gap-2 rounded-md bg-zinc-50 px-3 py-2 text-sm font-medium text-zinc-900 outline-offset-2 transition hover:bg-zinc-100 active:bg-zinc-100 active:text-zinc-900/60 active:transition-none dark:bg-zinc-800/50 dark:text-zinc-300 dark:hover:bg-zinc-800 dark:hover:text-zinc-50 dark:active:bg-zinc-800/50 dark:active:text-zinc-50/70"
				href="/">Go back home</a
			>
		</div>
	</Container>
{:else}
	<h1>{$page.status}: {$page.error?.message}</h1>
{/if}
