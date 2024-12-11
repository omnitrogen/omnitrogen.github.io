<script lang="ts">
	import ChevronRightIcon from '$lib/assets/logos/chevron-right-icon.svelte';

	export let Title: boolean = false;
	export let Description: boolean = false;
	export let Cta: boolean = false;
	export let Eyebrow: boolean = false;

	export let titleAs = 'h2';
	export let href = '';

	export let eyebrowAs = 'p';
	export let decorate = false;
	export let classStr = '';

	export let cardAs = 'div';
</script>

{#if Title}
	{#if href}
		<svelte:element
			this={titleAs}
			class="text-base font-semibold tracking-tight text-zinc-800 dark:text-zinc-100"
		>
			<div
				class="absolute -inset-x-4 -inset-y-6 z-0 scale-95 bg-zinc-50 opacity-0 transition group-hover:scale-100 group-hover:opacity-100 sm:-inset-x-6 sm:rounded-2xl dark:bg-zinc-800/50"
			/>
			<a {href}>
				<span class="absolute -inset-x-4 -inset-y-6 z-20 sm:-inset-x-6 sm:rounded-2xl" />
				<span class="relative z-10"><slot /></span>
			</a>
		</svelte:element>
	{:else}
		<svelte:element
			this={titleAs}
			class="text-base font-semibold tracking-tight text-zinc-800 dark:text-zinc-100"
		>
			<slot />
		</svelte:element>
	{/if}
{:else if Description}
	<p class="relative z-10 mt-2 text-sm text-zinc-600 dark:text-zinc-400">
		<slot />
	</p>
{:else if Cta}
	<div
		aria-hidden="true"
		class="relative z-10 mt-4 flex items-center text-sm font-medium text-teal-500"
	>
		<slot />
		<ChevronRightIcon />
	</div>
{:else if Eyebrow}
	<svelte:element
		this={eyebrowAs}
		class={`${classStr} relative z-10 order-first mb-3 flex items-center text-sm text-zinc-400 dark:text-zinc-500`}
		class:pl-3.5={decorate}
		{...$$restProps}
	>
		{#if decorate}
			<span class="absolute inset-y-0 left-0 flex items-center" aria-hidden="true">
				<span class="h-4 w-0.5 rounded-full bg-zinc-200 dark:bg-zinc-500" />
			</span>
		{/if}
		<slot />
	</svelte:element>
{:else}
	<svelte:element this={cardAs} class={`${classStr} group relative flex flex-col items-start`}>
		<slot />
	</svelte:element>
{/if}
