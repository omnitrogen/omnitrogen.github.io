<script lang="ts">
	import { page } from '$app/stores';

	let { navItems, ...restProps } = $props();
</script>

<nav {...restProps}>
	<ul
		class="text-sm-custom flex rounded-full bg-white/90 px-3 font-medium text-zinc-800 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur dark:bg-zinc-800/90 dark:text-zinc-200 dark:ring-white/10"
	>
		{#each navItems as navItem}
			<li>
				<a
					href={navItem.href}
					class="relative block px-3 py-2 transition {$page.url.pathname === navItem.href
						? 'text-teal-500 dark:text-teal-400'
						: 'hover:text-teal-500 dark:hover:text-teal-400'}"
				>
					{navItem.text}
					{#if $page.url.pathname === navItem.href}
						<span
							class="absolute inset-x-1 -bottom-px h-px bg-gradient-to-r from-teal-500/0 via-teal-500/40 to-teal-500/0 dark:from-teal-400/0 dark:via-teal-400/40 dark:to-teal-400/0"
						/>
					{/if}
				</a>
			</li>
		{/each}
	</ul>
</nav>

<style>
	.text-sm-custom {
		font-size: 0.875rem;
		line-height: 1.5rem;
	}
</style>
