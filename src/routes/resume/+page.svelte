<script lang="ts">
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
						src={Object.entries(imageModules).find((elt) => elt[0].includes(edu.logo))?.[1].default}
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
