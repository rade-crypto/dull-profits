import { geoAlbersUsa, geoPath } from 'd3-geo';
import { feature, mesh } from 'topojson-client';
import fs from 'fs';
const us = JSON.parse(fs.readFileSync('node_modules/us-atlas/states-10m.json', 'utf8'));
const states = feature(us, us.objects.states);
const proj = geoAlbersUsa().fitExtent([[80, 60], [1360, 860]], states);
const path = geoPath(proj);
const out = { all: states.features.map(f => ({ name: f.properties.name, d: path(f) })), pts: {} };
for (const [k, lonlat] of Object.entries({ LAX: [-118.408, 33.942], Riverside: [-117.396, 33.953], Chicago: [-87.63, 41.88], Birmingham: [-86.80, 33.52], Washington: [-77.04, 38.90] })) out.pts[k] = proj(lonlat);
// California close-up
const ca = states.features.find(f => f.properties.name === 'California');
const p2 = geoAlbersUsa().fitExtent([[60, 60], [700, 960]], ca); const path2 = geoPath(p2);
out.ca = { d: path2(ca), LAX: p2([-118.408, 33.942]), Riverside: p2([-117.396, 33.953]) };
fs.writeFileSync('map.json', JSON.stringify(out));
console.log(out.all.length, out.pts, out.ca.LAX);
