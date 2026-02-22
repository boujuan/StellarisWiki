/* --- Global Content Search --- */
let _searchTimer = null;

function onSearchInput() {
    clearTimeout(_searchTimer);
    const input = document.getElementById('global-search');
    const query = input.value.trim();
    document.getElementById('search-clear').style.display = query ? '' : 'none';
    if (query.length < 2) {
        document.getElementById('search-results').style.display = 'none';
        return;
    }
    _searchTimer = setTimeout(() => runSearch(query), 150);
}

function clearSearch() {
    document.getElementById('global-search').value = '';
    document.getElementById('search-clear').style.display = 'none';
    document.getElementById('search-results').style.display = 'none';
}

function runSearch(query) {
    const q = query.toLowerCase();
    const results = [];
    const seen = new Set();
    for (const [page, section, text] of SEARCH_INDEX) {
        const key = page + '|' + section;
        if (seen.has(key)) continue;
        const titleMatch = page.toLowerCase().includes(q) || section.toLowerCase().includes(q);
        const textLower = text.toLowerCase();
        const contentIdx = textLower.indexOf(q);
        if (!titleMatch && contentIdx < 0) continue;
        seen.add(key);
        let snippet = '';
        if (contentIdx >= 0) {
            const start = Math.max(0, contentIdx - 40);
            const end = Math.min(text.length, contentIdx + query.length + 80);
            snippet = (start > 0 ? '...' : '') +
                      text.slice(start, end) +
                      (end < text.length ? '...' : '');
        }
        results.push({page, section, snippet, titleMatch, contentIdx});
        if (results.length >= 30) break;
    }
    results.sort((a, b) => {
        if (a.titleMatch !== b.titleMatch) return a.titleMatch ? -1 : 1;
        return 0;
    });
    showSearchResults(results, query);
}

function showSearchResults(results, query) {
    const container = document.getElementById('search-results');
    if (results.length === 0) {
        container.innerHTML = '<div class="search-no-results">No results found</div>';
        container.style.display = '';
        return;
    }
    const escQ = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const re = new RegExp('(' + escQ + ')', 'gi');
    const esc = s => s.replace(/[<>&"]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;','"':'&quot;'})[c]);
    const escText = s => s.replace(/[<>&]/g, c => ({'<':'&lt;','>':'&gt;','&':'&amp;'})[c]);
    let html = '';
    for (const r of results) {
        const highlighted = r.snippet ? escText(r.snippet).replace(re, '<mark>$1</mark>') : '';
        const sectionLabel = r.section !== r.page
            ? '<span class="search-result-section"> &rsaquo; ' + escText(r.section) + '</span>' : '';
        html += '<div class="search-result" data-page="' + esc(r.page) + '">' +
                '<div class="search-result-title">' + escText(r.page) + sectionLabel + '</div>' +
                (highlighted ? '<div class="search-result-snippet">' + highlighted + '</div>' : '') +
                '</div>';
    }
    container.innerHTML = html;
    container.style.display = '';
}

document.getElementById('search-results').addEventListener('click', function(e) {
    const item = e.target.closest('.search-result');
    if (item && item.dataset.page) navigateToPage(item.dataset.page);
});

function navigateToPage(title) {
    // Close search results
    document.getElementById('search-results').style.display = 'none';
    // Find the row containing a link whose text matches the page title
    const allLinks = document.querySelectorAll('table a, table button[data-page]');
    let targetRow = null;
    for (const el of allLinks) {
        if (el.textContent.trim() === title ||
            (el.dataset && el.dataset.page === title)) {
            targetRow = el.closest('tr');
            if (targetRow) break;
        }
    }
    if (!targetRow) return;
    // Expand all ancestor section-body elements
    let node = targetRow;
    while (node) {
        node = node.parentElement;
        if (!node) break;
        if (node.classList && node.classList.contains('section-body') && !node.classList.contains('open')) {
            node.classList.add('open');
            const chevron = node.previousElementSibling?.querySelector('.chevron');
            if (chevron) chevron.style.transform = 'rotate(90deg)';
        }
    }
    // Scroll into view
    targetRow.scrollIntoView({behavior: 'smooth', block: 'center'});
    // Highlight
    targetRow.classList.remove('search-highlight');
    void targetRow.offsetWidth;  // force reflow to restart animation
    targetRow.classList.add('search-highlight');
}

document.addEventListener('click', function(e) {
    if (!e.target.closest('.search-bar')) {
        document.getElementById('search-results').style.display = 'none';
    }
});

/* --- Section Toggle --- */
function toggleSection(header) {
    const body = header.nextElementSibling;
    const chevron = header.querySelector('.chevron');
    if (!body || !body.classList.contains('section-body')) return;
    if (body.classList.contains('open')) {
        body.classList.remove('open');
        if (chevron) chevron.style.transform = 'rotate(0deg)';
    } else {
        body.classList.add('open');
        if (chevron) chevron.style.transform = 'rotate(90deg)';
    }
    saveDashboardState();
}

function expandAllSections() {
    document.querySelectorAll('.section-body').forEach(body => {
        body.classList.add('open');
        const chevron = body.previousElementSibling?.querySelector('.chevron');
        if (chevron) chevron.style.transform = 'rotate(90deg)';
    });
}

function collapseAllSections() {
    document.querySelectorAll('.section-body').forEach(body => {
        body.classList.remove('open');
        const chevron = body.previousElementSibling?.querySelector('.chevron');
        if (chevron) chevron.style.transform = 'rotate(0deg)';
    });
}

function filterTable(input, tableId) {
    const filter = input.value.toLowerCase();
    const table = document.getElementById(tableId);
    if (!table) return;
    table.querySelectorAll('tbody tr').forEach(row => {
        const matchesText = row.textContent.toLowerCase().includes(filter);
        const catHidden = row.dataset.catHidden === 'true';
        row.style.display = (matchesText && !catHidden) ? '' : 'none';
    });
}

function filterAllSubtables(input, sectionId) {
    const filter = input.value.toLowerCase();
    const section = document.getElementById(sectionId);
    if (!section) return;
    section.querySelectorAll('tbody tr').forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
    });
    section.querySelectorAll('.sub-section').forEach(sub => {
        const visible = sub.querySelectorAll('tbody tr:not([style*="display: none"])');
        sub.style.display = visible.length > 0 ? '' : 'none';
    });
}

function sortTable(tableId, colIndex) {
    const table = document.getElementById(tableId);
    if (!table) return;
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    const th = table.querySelectorAll('th')[colIndex];
    const dir = th.dataset.sortDir === 'asc' ? 'desc' : 'asc';
    table.querySelectorAll('th').forEach(h => {
        h.classList.remove('sort-asc', 'sort-desc');
        h.dataset.sortDir = 'none';
    });
    th.dataset.sortDir = dir;
    th.classList.add('sort-' + dir);
    rows.sort((a, b) => {
        let av = a.cells[colIndex]?.textContent.trim() || '';
        let bv = b.cells[colIndex]?.textContent.trim() || '';
        const an = parseFloat(av), bn = parseFloat(bv);
        if (!isNaN(an) && !isNaN(bn)) return dir === 'asc' ? an - bn : bn - an;
        return dir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av);
    });
    rows.forEach(row => tbody.appendChild(row));
}

/* --- Interactive Pie Charts --- */
const pieState = {};
const tooltip = null;

function initPie(canvasId, legendId, segments) {
    const canvas = document.getElementById(canvasId);
    const legend = document.getElementById(legendId);
    if (!canvas || !legend) return;

    const total = segments.reduce((s, d) => s + d.value, 0);
    if (total === 0) return;

    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    const size = 160;
    canvas.width = size * dpr;
    canvas.height = size * dpr;
    canvas.style.width = size + 'px';
    canvas.style.height = size + 'px';
    ctx.scale(dpr, dpr);

    const cx = size / 2, cy = size / 2, r = size / 2 - 4;
    const state = { segments, total, canvas, ctx, cx, cy, r, size, highlight: -1 };
    pieState[canvasId] = state;

    // Build legend items
    const h3 = legend.querySelector('h3');
    while (legend.lastChild !== h3) legend.removeChild(legend.lastChild);
    segments.forEach((seg, i) => {
        const row = document.createElement('div');
        row.dataset.index = i;
        row.innerHTML = '<span class="dot" style="background:' + seg.color + '"></span> '
            + seg.label + ' (' + seg.value + ')';
        row.addEventListener('mouseenter', () => { state.highlight = i; drawPie(state); row.classList.add('highlight'); });
        row.addEventListener('mouseleave', () => { state.highlight = -1; drawPie(state); row.classList.remove('highlight'); });
        legend.appendChild(row);
    });

    // Canvas hover
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left - cx, y = e.clientY - rect.top - cy;
        const dist = Math.sqrt(x * x + y * y);
        const tip = document.getElementById('pie-tooltip');
        if (dist > r) { state.highlight = -1; drawPie(state); tip.style.display = 'none'; clearLegendHighlight(legend); return; }
        let angle = Math.atan2(y, x) + Math.PI / 2;
        if (angle < 0) angle += Math.PI * 2;
        let cumAngle = 0;
        for (let i = 0; i < segments.length; i++) {
            cumAngle += (segments[i].value / total) * Math.PI * 2;
            if (angle <= cumAngle) {
                if (state.highlight !== i) { state.highlight = i; drawPie(state); setLegendHighlight(legend, i); }
                const pct = (segments[i].value / total * 100).toFixed(1);
                tip.textContent = segments[i].label + ': ' + segments[i].value + ' (' + pct + '%)';
                tip.style.display = 'block';
                tip.style.left = (e.clientX + 12) + 'px';
                tip.style.top = (e.clientY - 8) + 'px';
                return;
            }
        }
    });
    canvas.addEventListener('mouseleave', () => {
        state.highlight = -1; drawPie(state);
        document.getElementById('pie-tooltip').style.display = 'none';
        clearLegendHighlight(legend);
    });

    drawPie(state);
}

function drawPie(state) {
    const { segments, total, ctx, cx, cy, r, size, highlight } = state;
    ctx.clearRect(0, 0, size, size);
    let startAngle = -Math.PI / 2;
    segments.forEach((seg, i) => {
        const sliceAngle = (seg.value / total) * Math.PI * 2;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.arc(cx, cy, highlight === i ? r + 3 : r, startAngle, startAngle + sliceAngle);
        ctx.closePath();
        ctx.fillStyle = seg.color;
        ctx.globalAlpha = (highlight >= 0 && highlight !== i) ? 0.3 : 1;
        ctx.fill();
        ctx.globalAlpha = 1;
        startAngle += sliceAngle;
    });
}

function setLegendHighlight(legend, idx) {
    legend.querySelectorAll('div[data-index]').forEach(d => {
        d.classList.toggle('highlight', parseInt(d.dataset.index) === idx);
    });
}
function clearLegendHighlight(legend) {
    legend.querySelectorAll('div[data-index]').forEach(d => d.classList.remove('highlight'));
}

/* --- Global Category Filter --- */
const disabledCats = new Set();

function toggleCategoryFilter(chip) {
    const cat = chip.dataset.cat;
    if (disabledCats.has(cat)) {
        disabledCats.delete(cat);
        chip.classList.add('active');
    } else {
        disabledCats.add(cat);
        chip.classList.remove('active');
    }
    applyCategoryFilter();
}

function resetCategoryFilters() {
    disabledCats.clear();
    document.querySelectorAll('.cat-chip').forEach(c => c.classList.add('active'));
    applyCategoryFilter();
}

function disableAllCategoryFilters() {
    document.querySelectorAll('.cat-chip').forEach(c => {
        disabledCats.add(c.dataset.cat);
        c.classList.remove('active');
    });
    applyCategoryFilter();
}

function applyCategoryFilter() {
    if (disabledCats.size === 0) {
        // Fast path: nothing disabled, clear all catHidden
        document.querySelectorAll('tr[data-cat-hidden]').forEach(r => delete r.dataset.catHidden);
    } else {
        document.querySelectorAll('table tbody tr').forEach(row => {
            const tags = row.querySelectorAll('.tag[data-cat]');
            if (tags.length === 0) {
                // Row has no category tags — governed by the "none" filter
                if (disabledCats.has('__none__')) {
                    row.dataset.catHidden = 'true';
                } else {
                    delete row.dataset.catHidden;
                }
                return;
            }
            const rowCats = Array.from(tags).map(t => t.dataset.cat);
            const allDisabled = rowCats.every(c => disabledCats.has(c));
            if (allDisabled) {
                row.dataset.catHidden = 'true';
            } else {
                delete row.dataset.catHidden;
            }
        });
    }
    // Dim disabled tags everywhere
    document.querySelectorAll('.tag[data-cat]').forEach(tag => {
        tag.style.opacity = disabledCats.has(tag.dataset.cat) ? '0.3' : '';
    });
    // Re-run fetched table filter (respects catHidden)
    filterFetchedTable();
    // Re-run all other filterTable inputs (redirects, etc.)
    document.querySelectorAll('.filter-input').forEach(input => {
        const table = input.closest('.section-body')?.querySelector('table[id]');
        if (table && table.id !== 'fetched-table') filterTable(input, table.id);
    });
    // Re-run sub-table section visibility
    document.querySelectorAll('.sub-section').forEach(sub => {
        const visible = sub.querySelectorAll('tbody tr:not([style*="display: none"]):not([data-cat-hidden="true"])');
        sub.style.display = visible.length > 0 ? '' : 'none';
    });
    saveDashboardState();
}

/* --- Fetched Table Toggle Filter --- */
let fetchedFilterMode = 'all';
function setFetchedFilter(mode, btn) {
    fetchedFilterMode = mode;
    btn.closest('.toggle-group').querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    filterFetchedTable();
}
function filterFetchedTable() {
    const input = document.querySelector('#fetched .filter-input');
    const text = input ? input.value.toLowerCase() : '';
    document.querySelectorAll('#fetched-table tbody tr').forEach(row => {
        const matchesText = row.textContent.toLowerCase().includes(text);
        const matchesFilter = fetchedFilterMode === 'all' || row.dataset.source === 'main';
        const catHidden = row.dataset.catHidden === 'true';
        row.style.display = (matchesText && matchesFilter && !catHidden) ? '' : 'none';
    });
}

/* --- Page Add/Remove Management --- */
const pagesToAdd = new Set();
const pagesToRemove = new Set();

function toggleFetchPage(btn) {
    const page = btn.dataset.page;
    const isRemove = btn.classList.contains('fetch-btn-remove');
    if (isRemove) {
        if (pagesToRemove.has(page)) {
            pagesToRemove.delete(page);
            btn.classList.remove('toggled');
        } else {
            pagesToRemove.add(page);
            btn.classList.add('toggled');
        }
    } else {
        if (pagesToAdd.has(page)) {
            pagesToAdd.delete(page);
            btn.classList.remove('toggled');
        } else {
            pagesToAdd.add(page);
            btn.classList.add('toggled');
        }
    }
    updateCategoryCheckbox(btn);
    updatePendingBar();
    saveDashboardState();
}

function toggleCategory(checkbox, event) {
    event.stopPropagation();
    const subSection = checkbox.closest('.sub-section');
    if (!subSection) return;
    const buttons = subSection.querySelectorAll('.fetch-btn-add');
    const isChecked = checkbox.checked;
    buttons.forEach(btn => {
        const page = btn.dataset.page;
        if (isChecked && !pagesToAdd.has(page)) {
            pagesToAdd.add(page);
            btn.classList.add('toggled');
        } else if (!isChecked && pagesToAdd.has(page)) {
            pagesToAdd.delete(page);
            btn.classList.remove('toggled');
        }
    });
    updatePendingBar();
    saveDashboardState();
}

function updateCategoryCheckbox(btn) {
    const subSection = btn.closest('.sub-section');
    if (!subSection) return;
    const checkbox = subSection.querySelector('.cat-checkbox');
    if (!checkbox) return;
    const buttons = subSection.querySelectorAll('.fetch-btn-add');
    let total = 0, selected = 0;
    buttons.forEach(b => { total++; if (pagesToAdd.has(b.dataset.page)) selected++; });
    if (selected === 0) { checkbox.checked = false; checkbox.indeterminate = false; }
    else if (selected === total) { checkbox.checked = true; checkbox.indeterminate = false; }
    else { checkbox.checked = false; checkbox.indeterminate = true; }
}

function updatePendingBar() {
    const bar = document.getElementById('pending-bar');
    const info = document.getElementById('pending-info');
    const total = pagesToAdd.size + pagesToRemove.size;
    if (total === 0) {
        bar.classList.remove('visible');
        return;
    }
    const parts = [];
    if (pagesToAdd.size) parts.push(pagesToAdd.size + ' to add');
    if (pagesToRemove.size) parts.push(pagesToRemove.size + ' to remove');
    info.textContent = parts.join(', ');
    bar.classList.add('visible');
}

function discardPageChanges() {
    pagesToAdd.clear();
    pagesToRemove.clear();
    document.querySelectorAll('.fetch-btn.toggled').forEach(b => b.classList.remove('toggled'));
    document.querySelectorAll('.cat-checkbox').forEach(cb => { cb.checked = false; cb.indeterminate = false; });
    updatePendingBar();
    saveDashboardState();
}

function downloadUpdatedConfig() {
    const yaml = typeof CONFIG_YAML !== 'undefined' ? CONFIG_YAML : '';
    if (!yaml) return;

    // Modify config in-place: remove deleted pages, append new pages at section end
    const toAdd = new Set(pagesToAdd);
    const lines = yaml.split('\n');
    const outLines = [];
    let inPages = false;
    let insertionDone = false;

    for (const line of lines) {
        if (/^pages_to_fetch:/.test(line)) {
            inPages = true;
            outLines.push(line);
            continue;
        }
        if (inPages) {
            // Non-indented non-empty line means we left the section
            if (/^\S/.test(line) && line.trim() !== '') {
                // Append new pages before leaving
                if (!insertionDone) {
                    toAdd.forEach(p => outLines.push('  - "' + p + '"'));
                    insertionDone = true;
                }
                inPages = false;
                outLines.push(line);
                continue;
            }
            // Inside section: check if this is a page entry
            const m = line.match(/^\s+-\s+"(.+)"/);
            if (m) {
                if (pagesToRemove.has(m[1])) continue;   // skip removed pages
                toAdd.delete(m[1]);                       // already exists, don't re-add
            }
            outLines.push(line);  // keep comments, blank lines, and remaining entries
            continue;
        }
        outLines.push(line);
    }
    // If file ended while still in pages section
    if (inPages && !insertionDone) {
        toAdd.forEach(p => outLines.push('  - "' + p + '"'));
    }

    const output = outLines.join('\n');

    const blob = new Blob([output], {type: 'text/yaml'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'config.yaml';
    a.click();
    URL.revokeObjectURL(a.href);

    // Show instructions if on remote
    if (window.location.protocol !== 'file:') {
        showModal('remote-instructions-modal');
    }
}

/* --- Modal --- */
function showModal(id) {
    document.getElementById(id).classList.add('visible');
}
function hideModal(id) {
    document.getElementById(id).classList.remove('visible');
}
function copyCode(btn) {
    const pre = btn.parentElement.querySelector('pre');
    navigator.clipboard.writeText(pre.textContent).then(() => {
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 2000);
    });
}

// --- localStorage persistence ---
const _STORAGE_KEY = 'stellaris-wiki-dashboard';
const _STORAGE_VER_KEY = 'stellaris-wiki-dashboard-ver';

function saveDashboardState() {
    try {
        const state = {
            pagesToAdd: Array.from(pagesToAdd),
            pagesToRemove: Array.from(pagesToRemove),
            disabledCats: Array.from(disabledCats),
            expandedSections: [],
        };
        document.querySelectorAll('.section-body.open').forEach(body => {
            const sec = body.closest('section') || body.closest('.sub-section');
            const id = sec?.id || sec?.dataset?.category || '';
            if (id) state.expandedSections.push(id);
        });
        localStorage.setItem(_STORAGE_KEY, JSON.stringify(state));
        localStorage.setItem(_STORAGE_VER_KEY, GENERATED_AT);
    } catch (e) { /* localStorage unavailable */ }
}

function restoreDashboardState() {
    try {
        if (localStorage.getItem(_STORAGE_VER_KEY) !== GENERATED_AT) {
            localStorage.removeItem(_STORAGE_KEY);
            return;
        }
        const raw = localStorage.getItem(_STORAGE_KEY);
        if (!raw) return;
        const state = JSON.parse(raw);

        // Restore pagesToAdd
        (state.pagesToAdd || []).forEach(page => {
            const btn = document.querySelector('.fetch-btn-add[data-page="' + CSS.escape(page) + '"]');
            if (btn) { pagesToAdd.add(page); btn.classList.add('toggled'); }
        });
        // Restore pagesToRemove
        (state.pagesToRemove || []).forEach(page => {
            const btn = document.querySelector('.fetch-btn-remove[data-page="' + CSS.escape(page) + '"]');
            if (btn) { pagesToRemove.add(page); btn.classList.add('toggled'); }
        });
        updatePendingBar();

        // Restore category checkboxes
        document.querySelectorAll('.cat-checkbox').forEach(cb => {
            const btn = cb.closest('.sub-section')?.querySelector('.fetch-btn-add');
            if (btn) updateCategoryCheckbox(btn);
        });

        // Restore disabled category filters
        if (state.disabledCats && state.disabledCats.length > 0) {
            state.disabledCats.forEach(cat => {
                disabledCats.add(cat);
                const chip = document.querySelector('.cat-chip[data-cat="' + CSS.escape(cat) + '"]');
                if (chip) chip.classList.remove('active');
            });
            applyCategoryFilter();
        }

        // Restore section expand/collapse
        if (state.expandedSections) {
            const expanded = new Set(state.expandedSections);
            document.querySelectorAll('.section, .sub-section').forEach(sec => {
                const id = sec.id || sec.dataset?.category || '';
                if (!id) return;
                const body = sec.querySelector(':scope > .section-body');
                const header = sec.querySelector(':scope > .section-header, :scope > .sub-header');
                if (!body || !header) return;
                const chevron = header.querySelector('.chevron');
                if (expanded.has(id)) {
                    body.classList.add('open');
                    if (chevron) chevron.style.transform = 'rotate(90deg)';
                } else {
                    body.classList.remove('open');
                    if (chevron) chevron.style.transform = 'rotate(0deg)';
                }
            });
        }
    } catch (e) { /* ignore restore errors */ }
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.section-body.open').forEach(body => {
        const chevron = body.previousElementSibling?.querySelector('.chevron');
        if (chevron) chevron.style.transform = 'rotate(90deg)';
    });
    // Make .tag spans in tables clickable to toggle their category
    document.addEventListener('click', (e) => {
        const tag = e.target.closest('.tag[data-cat]');
        if (!tag || tag.closest('.cat-filter-bar')) return;
        const cat = tag.dataset.cat;
        const chip = document.querySelector('.cat-chip[data-cat="' + CSS.escape(cat) + '"]');
        if (chip) toggleCategoryFilter(chip);
    });
    // Close modals on overlay click
    document.querySelectorAll('.modal-overlay').forEach(overlay => {
        overlay.addEventListener('click', (e) => {
            if (e.target === overlay) overlay.classList.remove('visible');
        });
    });
    // Restore saved state (overrides defaults)
    restoreDashboardState();
});
