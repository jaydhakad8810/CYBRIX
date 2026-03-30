function AnalyzerForm({
  inputValue,
  mode,
  isLoading,
  onInputChange,
  onModeChange,
  onSubmit,
}) {
  return (
    <form
      className="space-y-4 rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-2xl shadow-slate-950/30 backdrop-blur"
      onSubmit={onSubmit}
    >
      <div className="space-y-2">
        <label className="text-sm font-medium text-slate-300" htmlFor="analysis-mode">
          Analysis Type
        </label>
        <select
          id="analysis-mode"
          className="w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-green-500"
          value={mode}
          onChange={(event) => onModeChange(event.target.value)}
        >
          <option value="link">Link</option>
          <option value="message">Message</option>
        </select>
      </div>

      <div className="space-y-2">
        <label className="text-sm font-medium text-slate-300" htmlFor="analysis-input">
          Enter URL or text
        </label>
        <textarea
          id="analysis-input"
          className="min-h-40 w-full rounded-xl border border-slate-700 bg-slate-950 px-4 py-3 text-slate-100 outline-none transition focus:border-green-500"
          placeholder="Paste a suspicious URL or message here..."
          value={inputValue}
          onChange={(event) => onInputChange(event.target.value)}
        />
      </div>

      <button
        className="w-full rounded-xl bg-green-500 px-4 py-3 font-semibold text-slate-950 transition hover:bg-green-400 disabled:cursor-not-allowed disabled:bg-green-900 disabled:text-slate-300"
        disabled={isLoading}
        type="submit"
      >
        {isLoading ? "Analyzing..." : "Analyze"}
      </button>
    </form>
  );
}

export default AnalyzerForm;
