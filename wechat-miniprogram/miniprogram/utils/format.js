function formatStars(value) {
  var number = Number(value || 0);
  if (number >= 1000000) return (number / 1000000).toFixed(2) + "m";
  if (number >= 1000) return (number / 1000).toFixed(1) + "k";
  return String(number);
}

function formatDelta(value, baseline) {
  if (!baseline || value === null || value === undefined) return "基线";
  return (Number(value) >= 0 ? "+" : "") + Number(value).toFixed(0);
}

function formatGrowth(value, baseline) {
  if (!baseline || value === null || value === undefined) return "-";
  return (Number(value) >= 0 ? "+" : "") + Number(value).toFixed(2) + "%";
}

function activityLabel(value) {
  if (Number(value || 0) >= 85) return "活跃";
  if (Number(value || 0) >= 60) return "稳定";
  if (Number(value || 0) >= 30) return "偏慢";
  return "沉寂";
}

module.exports = { formatStars: formatStars, formatDelta: formatDelta, formatGrowth: formatGrowth, activityLabel: activityLabel };
