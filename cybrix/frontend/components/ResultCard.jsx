function ResultCard({ result, error }) {
  if (error) {
    return (
      <section className="rounded-2xl border border-red-900/80 bg-red-950/40 p-6 text-red-200">
        <h2 className="text-lg font-semibold">Request Error</h2>
        <p className="mt-2 text-sm">{error}</p>
      </section>
    );
  }

  if (!result) {
    return (
      <section className="rounded-2xl border border-dashed border-slate-700 bg-slate-900/40 p-6 text-slate-400">
        <h2 className="text-lg font-semibold text-slate-200">Result</h2>
        <p className="mt-2 text-sm">
          The placeholder analysis response will appear here after you submit the form.
        </p>
      </section>
    );
  }

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6 shadow-xl shadow-slate-950/20">
      <h2 className="text-lg font-semibold text-slate-100">Result</h2>
      <div className="mt-4 grid gap-4 sm:grid-cols-3">
        <div className="rounded-xl bg-slate-950/80 p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Risk</p>
          <p className="mt-2 text-2xl font-bold text-green-400">{result.risk}</p>
        </div>
        <div className="rounded-xl bg-slate-950/80 p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Reason</p>
          <p className="mt-2 text-sm text-slate-200">{result.reason}</p>
        </div>
        <div className="rounded-xl bg-slate-950/80 p-4">
          <p className="text-xs uppercase tracking-[0.2em] text-slate-500">Action</p>
          <p className="mt-2 text-sm text-slate-200">{result.action}</p>
        </div>
      </div>
    </section>
  );
}

export default ResultCard;
