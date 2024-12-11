<script lang="ts">
	import profile from '$lib/assets/images/profile.webp';
	import { page } from '$app/stores';
	import DesktopNavigation from '$lib/components/DesktopNavigation.svelte';
	import LanguageToggle from '$lib/components/LanguageToggle.svelte';
	import MobileNavigation from '$lib/components/MobileNavigation.svelte';
	import { i18n } from '$lib/i18n';
	import BlurFade from '$lib/components/BlurFade.svelte';
	import * as m from '$lib/paraglide/messages.js';

	let isHomePage = $derived(i18n.route($page.url.pathname) === '/');

	type NavItem = {
		href: string;
		text: string;
	};

	const navItems: NavItem[] = $state([
		{ href: '/about', text: m.about() },
		{ href: '/projects', text: m.projects() },
		{ href: '/resume', text: m.resume() },
		{ href: '/uses', text: 'Uses' }
	]);
</script>

<header
	class="pointer-events-none relative z-50 flex flex-col"
	style="--header-height: var(--header-height); --header-mb: var(--header-mb);"
>
	{#if isHomePage}
		<div class="order-last mt-[calc(theme(spacing.16)-theme(spacing.3))]"></div>
		<div class="top-0 order-last -mb-3 pt-3 sm:px-8" style="position: var(--header-position);">
			<div class="mx-auto max-w-7xl lg:px-8">
				<div class="relative px-4 sm:px-8 lg:px-12">
					<div class="mx-auto max-w-2xl lg:max-w-5xl">
						<div
							class="top-[var(--avatar-top,theme(spacing.3))] w-full"
							style="position: var(--header-inner-position);"
						>
							<div class="relative">
								<BlurFade once={true}>
									<div
										class="absolute left-0 top-3 h-10 w-10 origin-left rounded-full bg-white/90 p-0.5 shadow-lg shadow-zinc-800/5 ring-1 ring-zinc-900/5 backdrop-blur transition-opacity dark:bg-zinc-800/90 dark:ring-white/10"
										style="opacity: var(--avatar-border-opacity, 0); transform: var(--avatar-border-transform);"
									></div>
									<a
										href="/"
										aria-label="Home"
										class="pointer-events-auto block h-16 w-16 origin-left"
									>
										<img
											src={profile}
											alt=""
											sizes="4rem"
											class={'h-16 w-16 rounded-full bg-zinc-100 object-cover dark:bg-zinc-800'}
										/>
									</a>
								</BlurFade>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	{/if}
	<div class="top-0 z-10 h-16 pt-6" style="position: var(--header-position);">
		<div
			class="top-[var(--header-top,theme(spacing.6))] w-full sm:px-8"
			style="position: var(--header-inner-position);"
		>
			<div class="mx-auto max-w-7xl lg:px-8">
				<div class="relative px-4 sm:px-8 lg:px-12">
					<div class="mx-auto max-w-4xl lg:max-w-5xl">
						<div class="relative flex gap-4">
							<div class="flex flex-1">
								{#if !isHomePage}
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
								{/if}
							</div>
							<div class="flex flex-1 justify-end md:justify-center">
								<MobileNavigation {navItems} class="pointer-events-auto md:hidden" />
								<DesktopNavigation {navItems} class="pointer-events-auto hidden md:block" />
							</div>
							<div class="flex justify-end md:flex-1">
								<div class="pointer-events-auto">
									<LanguageToggle />
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</header>
