<script lang="ts">
	import Container from '$lib/components/Container.svelte';
	import * as m from '$lib/paraglide/messages.js';
	import BlurFade from '$lib/components/BlurFade.svelte';
	import SocialIcons from '$lib/components/SocialIcons.svelte';
	import { Separator } from '$lib/components/ui/separator/index.js';

	import CodeXml from 'lucide-svelte/icons/code-xml';
	import Heart from 'lucide-svelte/icons/heart';
</script>

<footer class="mb-24 mt-24 pt-4 md:mb-6">
	<BlurFade once={true}>
		<div>
			<Separator
				class="mx-auto mb-4 h-0.5 w-3/4 rounded-full bg-zinc-900/5 md:mb-8 dark:bg-white/10"
			/>
		</div>
		<div class="flex flex-col items-center justify-between gap-6">
			<div class="flex gap-6 text-sm font-medium text-zinc-800 dark:text-zinc-200">
				<a class="transition hover:text-teal-500 dark:hover:text-teal-400" href="/about">About</a>
				<a class="transition hover:text-teal-500 dark:hover:text-teal-400" href="/projects"
					>Projects</a
				>
				<a class="transition hover:text-teal-500 dark:hover:text-teal-400" href="/speaking"
					>Speaking</a
				>
				<a class="transition hover:text-teal-500 dark:hover:text-teal-400" href="/uses">Uses</a>
			</div>

			<div class="flex gap-6">
				<a class="group -m-1 p-1" aria-label="Follow on Twitter" href="https://twitter.com">
					<SocialIcons
						Twitter
						class="h-6 w-6 fill-zinc-500 transition group-hover:fill-zinc-600 dark:fill-zinc-400 dark:group-hover:fill-zinc-300"
					/>
				</a>
				<a class="group -m-1 p-1" aria-label="Follow on Instagram" href="https://instagram.com">
					<SocialIcons
						Instagram
						class="h-6 w-6 fill-zinc-500 transition group-hover:fill-zinc-600 dark:fill-zinc-400 dark:group-hover:fill-zinc-300"
					/>
				</a>
				<a class="group -m-1 p-1" aria-label="Follow on GitHub" href="https://github.com">
					<SocialIcons
						GitHub
						class="h-6 w-6 fill-zinc-500 transition group-hover:fill-zinc-600 dark:fill-zinc-400 dark:group-hover:fill-zinc-300"
					/>
				</a>
				<a class="group -m-1 p-1" aria-label="Follow on LinkedIn" href="https://linkedin.com">
					<SocialIcons
						LinkedIn
						class="h-6 w-6 fill-zinc-500 transition group-hover:fill-zinc-600 dark:fill-zinc-400 dark:group-hover:fill-zinc-300"
					/>
				</a>
			</div>
			<div class="flex flex-row text-sm text-zinc-400 dark:text-zinc-500">
				<CodeXml size={24} class="px-1" />
				{m.footerWith()}
				<Heart size={22} class="px-1" />{m.footerBy()}
			</div>
		</div>
	</BlurFade>
</footer>
