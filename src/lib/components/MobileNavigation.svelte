<script lang="ts">
	import { fade, scale } from 'svelte/transition';
	import X from 'lucide-svelte/icons/x';
	import * as Sheet from '$lib/components/ui/sheet/index.js';

	let open = $state(false);

	let { navItems, ...restProps } = $props();
</script>

<div {...restProps}>
	<Sheet.Root bind:open>
		<Sheet.Trigger>
			<button
				class="text-md rounded-full border-transparent bg-white/90 px-4 py-2 font-medium text-zinc-800 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur focus:border-transparent focus:ring-0 dark:bg-zinc-800/90 dark:text-zinc-200 dark:ring-white/10 dark:hover:ring-white/20"
				type="button"
			>
				Menu
			</button>
		</Sheet.Trigger>

		<Sheet.Content class="rounded-l-xl">
			<nav class="p-4">
				<ul class="-my-2 text-end text-base text-zinc-800 dark:text-zinc-300">
					{#each navItems as navItem}
						<li>
							<a class="block py-2" href={navItem.href} onclick={() => (open = false)}
								>{navItem.text}
							</a>
						</li>
					{/each}
				</ul>
			</nav>
		</Sheet.Content>
	</Sheet.Root>
</div>
