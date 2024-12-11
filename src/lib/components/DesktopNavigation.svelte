<script lang="ts">
	import profile from '$lib/assets/images/profile.webp';
	import { page } from '$app/state';
	import LanguageToggle from '$lib/components/LanguageToggle.svelte';
	import { cn } from '$lib/utils';
	import type { NavItem } from '$lib/types';
	import { i18n } from '$lib/i18n';

	let {
		navItems,
		isHomePage,
		...restProps
	}: { navItems: NavItem[]; isHomePage: boolean; [x: string]: unknown } = $props();
</script>

<div {...restProps}>
	<div class="relative mx-auto my-8 w-full max-w-7xl px-4 sm:px-8">
		<div class="relative px-8 sm:px-12 lg:px-24">
			<div class="mx-auto max-w-4xl lg:max-w-5xl">
				<div class="relative flex justify-between">
					<div
						class={cn(
							'h-12 w-12 rounded-full p-0.5',
							!isHomePage &&
								'bg-white/90 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur dark:bg-zinc-800/90 dark:ring-white/10'
						)}
					>
						{#if !isHomePage}
							<a href="/" aria-label="Home" class="pointer-events-auto">
								<img
									src={profile}
									alt=""
									sizes="2.25rem"
									class="h-11 w-11 rounded-full bg-zinc-100 object-cover dark:bg-zinc-800"
								/>
							</a>
						{/if}
					</div>
					<div class="pointer-events-auto">
						<nav>
							<ul
								class="text-sm-custom flex rounded-full bg-white/90 px-3 font-medium text-zinc-800 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur dark:bg-zinc-800/90 dark:text-zinc-200 dark:ring-white/10"
							>
								{#each navItems as navItem}
									<li>
										<a
											href={navItem.href}
											class={cn(
												'relative block px-3 py-2 transition',
												i18n.route(page.url.pathname) === navItem.href &&
													'text-teal-500 dark:text-teal-400',
												!(i18n.route(page.url.pathname) === navItem.href) &&
													'hover:text-teal-500 dark:hover:text-teal-400'
											)}
										>
											{navItem.text}
											{#if i18n.route(page.url.pathname) === navItem.href}
												<span
													class="absolute inset-x-1 -bottom-px h-px bg-gradient-to-r from-teal-500/0 via-teal-500/40 to-teal-500/0 dark:from-teal-400/0 dark:via-teal-400/40 dark:to-teal-400/0"
												></span>
											{/if}
										</a>
									</li>
								{/each}
							</ul>
						</nav>
					</div>
					<div class="pointer-events-auto">
						<LanguageToggle />
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
