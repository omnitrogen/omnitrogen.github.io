<script lang="ts">
	import profile from '$lib/assets/images/profile.webp';
	import LanguageToggle from '$lib/components/LanguageToggle.svelte';
	import * as Drawer from '$lib/components/ui/drawer/index.js';
	import type { NavItem } from '$lib/types';
	import { fly } from 'svelte/transition';

	let open = $state(false);

	let visible = $state(true);

	let hash_changed = false;
	function handle_hashchange() {
		hash_changed = true;
	}

	let last_scroll = 0;
	function handle_scroll() {
		const scroll = window.scrollY;
		if (!hash_changed) {
			visible = scroll === last_scroll ? visible : scroll < 50 || scroll < last_scroll;
		}

		last_scroll = scroll;
		hash_changed = false;
	}

	let { navItems, ...restProps }: { navItems: NavItem[]; [x: string]: unknown } = $props();
</script>

<svelte:window
	onscroll={handle_scroll}
	onhashchange={handle_hashchange}
	onkeydown={(e) => {
		if (open && e.key === 'Escape') {
			open = false;
		}
	}}
/>

{#if visible}
	<div in:fly>
		<div {...restProps}>
			<div
				class="fixed bottom-0 z-40 mx-auto w-full max-w-7xl bg-white py-4 shadow-md ring-1 ring-zinc-900/5 sm:px-8 dark:bg-zinc-800 dark:ring-white/10"
			>
				<div class="relative px-4 sm:px-8 lg:px-12">
					<div class="mx-auto max-w-4xl lg:max-w-5xl">
						<div class="relative flex justify-between gap-6">
							<div class="pointer-events-auto">
								<LanguageToggle />
							</div>

							<div class="flex gap-6">
								<div class="pointer-events-auto">
									<Drawer.Root bind:open>
										<div>
											<Drawer.Trigger>
												<button
													class="text-md rounded-full border-transparent bg-white/90 px-4 py-2 font-medium text-zinc-800 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur focus:border-transparent focus:ring-0 dark:bg-zinc-800/90 dark:text-zinc-200 dark:ring-white/10 dark:hover:ring-white/20"
													type="button"
												>
													Menu
												</button>
											</Drawer.Trigger>

											<Drawer.Content
												class="border-zinc-800 focus:ring-0 focus:ring-offset-0 dark:bg-zinc-800"
											>
												<nav class="m-4">
													<ul class="py-6 text-end text-2xl text-zinc-800 dark:text-zinc-300">
														{#each navItems as navItem}
															<li>
																<a
																	class="block px-4 py-4"
																	href={navItem.href}
																	onclick={() => {
																		open = false;
																		visible = true;
																	}}
																>
																	<b>{navItem.text}</b>
																</a>
															</li>
														{/each}
													</ul>
												</nav>
											</Drawer.Content>
										</div>
									</Drawer.Root>
								</div>
								<div
									class="h-10 w-10 rounded-full bg-white/90 p-0.5 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur dark:bg-zinc-800/90 dark:ring-white/10"
								>
									<a href="/" aria-label="Home" class="pointer-events-auto">
										<img
											src={profile}
											alt=""
											sizes="2.25rem"
											class="h-9 w-9 rounded-full bg-zinc-100 object-cover dark:bg-zinc-800"
										/>
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
{/if}
