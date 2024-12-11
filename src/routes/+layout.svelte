<script lang="ts">
	import { page } from '$app/state';
	import '../app.css';
	import Header from '$lib/components/Header.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import { ModeWatcher } from 'mode-watcher';
	import { i18n } from '$lib/i18n';
	import { ParaglideJS } from '@inlang/paraglide-sveltekit';

	let { children } = $props();
	let errorPage = $derived(page.error?.message === 'Not Found');
</script>

<ModeWatcher />

<ParaglideJS {i18n}>
	<div class="fixed inset-0 flex justify-center sm:px-8">
		<div class="flex w-full max-w-7xl lg:px-8">
			<div
				class="w-full bg-white ring-1 ring-zinc-100 dark:bg-zinc-900 dark:ring-zinc-300/20"
			></div>
		</div>
	</div>

	<div class={`relative ${errorPage ? 'flex w-full flex-col' : ''}`}>
		<Header />

		<main class:flex-auto={errorPage}>
			{@render children()}
		</main>

		<Footer />
	</div>
</ParaglideJS>
