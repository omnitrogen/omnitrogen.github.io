<script lang="ts">
	import SimpleLayout from '$lib/components/SimpleLayout.svelte';
	import Speaking from '$lib/components/Speaking.svelte';

	import * as m from '$lib/paraglide/messages.js';
	import { languageTag } from '$lib/paraglide/runtime.js';
	import { resume } from '$content/resume';

	import MoveRight from 'lucide-svelte/icons/move-right';
	import Dot from 'lucide-svelte/icons/dot';
	import ListCollapse from 'lucide-svelte/icons/list-collapse';

	const imageModules = import.meta.glob(
		'$lib/assets/images/*.{avif,gif,heif,jpeg,jpg,png,tiff,webp,svg}',
		{
			eager: true,
			query: {
				enhanced: true
			}
		}
	);
</script>

<svelte:head>
	<title>Speaking - Félix Defrance</title>
	<meta
		name="description"
		content="I’ve spoken at events all around the world and been interviewed for many podcasts."
	/>
</svelte:head>

<SimpleLayout
	title="I’ve spoken at events all around the world and been interviewed for many podcasts."
	intro="One of my favorite ways to share my ideas is live on stage, where there’s so much more communication bandwidth than there is in writing, and I love podcast interviews because they give me the opportunity to answer questions instead of just present my opinions."
>
	<div class="space-y-20">
		<Speaking SpeakingSection title="Conferences">
			<Speaking
				Appearance
				href="#"
				title="In space, no one can watch you stream — until now"
				description="A technical deep-dive into HelioStream, the real-time streaming library I wrote for transmitting live video back to Earth."
				event="SysConf 2021"
				cta="Watch video"
			/>
			<Speaking
				Appearance
				href="#"
				title="Lessons learned from our first product recall"
				description="They say that if you’re not embarassed by your first version, you’re doing it wrong. Well when you’re selling DIY space shuttle kits it turns out it’s a bit more complicated."
				event="Business of Startups 2020"
				cta="Watch video"
			/>
		</Speaking>
		<Speaking SpeakingSection title="Podcasts">
			<Speaking
				Appearance
				href="#"
				title="Using design as a competitive advantage"
				description="How we used world-class visual design to attract a great team, win over customers, and get more press for Planetaria."
				event="Encoding Design, July 2022"
				cta="Listen to podcast"
			/>
			<Speaking
				Appearance
				href="#"
				title="Bootstrapping an aerospace company to $17M ARR"
				description="The story of how we built one of the most promising space startups in the world without taking any capital from investors."
				event="The Escape Velocity Show, March 2022"
				cta="Listen to podcast"
			/>
			<Speaking
				Appearance
				href="#"
				title="Programming your company operating system"
				description="On the importance of creating systems and processes for running your business so that everyone on the team knows how to make the right decision no matter the situation."
				event="How They Work Radio, September 2021"
				cta="Listen to podcast"
			/>
		</Speaking>

		<section>
			<h1>{m.work()}</h1>
			<br />

			{#each resume.languages[languageTag()].work as work}
				<article>
					<hgroup>
						<h4>{work.name} {work.nameExplanation !== null ? `(${work.nameExplanation})` : ''}</h4>
						<br />
						<h5><mark>{work.title}</mark></h5>
						<br />
						<small><kbd>{work.date}</kbd></small>
					</hgroup>

					{#if work.description?.length}
						<details>
							<summary><ListCollapse /></summary>
							<blockquote>
								{#each work.description as item}
									<small><b>{item.mark}</b> <Dot /> {item.text}</small><br />
								{/each}
							</blockquote>
						</details>
					{/if}
				</article>
				<br />
			{/each}

			<br />

			<h1>{m.education()}</h1>

			<br />

			{#each resume.languages[languageTag()].education as edu}
				<article>
					<hgroup>
						<div style="display: flex; flex-direction: row;">
							<img
								src={Object.entries(imageModules).find((elt) => elt[0].includes(edu.logo))?.[1]
									.default}
								alt=""
								style="width: 10rem;"
							/>
							<h4>{edu.name} {edu.nameExplanation !== null ? `(${edu.nameExplanation})` : ''}</h4>
						</div>
						<br />
						<h5><mark>{edu.title}</mark></h5>
						<br />
						<small><kbd>{edu.startDate} <MoveRight /> {edu.endDate}</kbd></small>
					</hgroup>

					{#if edu.description?.length}
						<details>
							<summary><ListCollapse /></summary>
							<blockquote>
								{#each edu.description as item}
									<small><b>{item.mark}</b> <Dot /> {item.text}</small><br />
								{/each}
							</blockquote>
						</details>
					{/if}
				</article>
				<br />
			{/each}
		</section>
	</div>
</SimpleLayout>
